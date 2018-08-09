module.exports = {
    "env": {
        "browser": true,
        "commonjs": true,
        "es6": true
    },
    "extends": "eslint:recommended",
    "parserOptions": {
        "ecmaVersion": 2015
    },
    "rules": {
        "indent": [
            "error",
            4
        ],
        "linebreak-style": [
            "error",
            "windows"
        ],
        "quotes": [
            "warn",
            "double"
        ],
        "semi": [
            "error",
            "always"
        ],
        "space-infix-ops": [
        	"error", 
        	{"int32Hint": false}
        ],
        "no-trailing-spaces": [
        	"error", 
        	{ "skipBlankLines": false}
        ]
    }
};
