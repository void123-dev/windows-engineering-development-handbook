-- Keep DOCX tables inside the 6x9-inch print-preview text area.
-- Pandoc's DOCX writer uses a 7920-twip table baseline. The reference DOCX
-- provides 6429 twips between the inside/outside margins, so column fractions
-- intentionally total 0.80 and leave a small safety margin.

local MAX_TABLE_FRACTION = 0.80
local MIN_COLUMN_FRACTION = 0.15

local function cell_text_length(cell)
  return #pandoc.utils.stringify(cell.contents)
end

function Table(table)
  local column_count = #table.colspecs
  if column_count == 0 then
    return table
  end

  local weights = {}
  for column = 1, column_count do
    weights[column] = 1
  end

  local function measure_rows(rows)
    for _, row in ipairs(rows) do
      for column, cell in ipairs(row.cells) do
        if column <= column_count then
          weights[column] = math.max(weights[column], cell_text_length(cell))
        end
      end
    end
  end

  measure_rows(table.head.rows)
  for _, body in ipairs(table.bodies) do
    measure_rows(body.head)
    measure_rows(body.body)
  end
  measure_rows(table.foot.rows)

  local total_weight = 0
  for column = 1, column_count do
    total_weight = total_weight + weights[column]
  end

  local minimum = math.min(MIN_COLUMN_FRACTION, MAX_TABLE_FRACTION / column_count)
  local proportional_space = MAX_TABLE_FRACTION - minimum * column_count
  for column = 1, column_count do
    local alignment = table.colspecs[column][1]
    local proportional_width = minimum
    if proportional_space > 0 then
      proportional_width = proportional_width + proportional_space * weights[column] / total_weight
    end
    table.colspecs[column] = {alignment, proportional_width}
  end

  return table
end

function Pandoc(document)
  local blocks = pandoc.List()
  for index, block in ipairs(document.blocks) do
    local next_block = document.blocks[index + 1]
    if block.t == "Header" and next_block and next_block.t == "Table" then
      blocks:insert(pandoc.RawBlock(
        "openxml",
        '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
      ))
    end
    blocks:insert(block)
  end
  document.blocks = blocks
  return document
end
