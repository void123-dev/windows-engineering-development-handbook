# Composer

{

	"name": "",

	"description": "",

	"type": "wordpress-plugin",

	"license": "GPL-2.0-or-later",

	"require": {

		"php": "\>=8.2"

	},

	"require-dev": {

		"dealerdirect/phpcodesniffer-composer-installer": "^1.0",

		"wp-coding-standards/wpcs": "^3.0",

		"phpcompatibility/phpcompatibility-wp": "^2.1",

		"phpstan/phpstan": "^2.1",

		"szepeviktor/phpstan-wordpress": "^2.0"

	},

	"autoload": {

		"psr-4": {

			"": "src/"

		}

	},

	"scripts": {

		"lint": "phpcs",

		"lint:fix": "phpcbf",

		"analyse": "phpstan analyse",

		"quality": \[

			"@lint",

			"@analyse"

		\]

	},

	"config": {

		"allow-plugins": {

			"dealerdirect/phpcodesniffer-composer-installer": true

		},

		"sort-packages": true

	}

}

