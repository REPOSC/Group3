call vagrant plugin install vagrant-vbguest
call npm install --save-dev mocha
call cd frontend
call npm install
call npm install --save-dev axios
call npm install --save-dev eslint eslint-plugin-vue@next
call npm install --save-dev stylelint stylelint-order
call cd ../frontend2
call npm install
call npm install flyio
call npm install --save-dev eslint eslint-plugin-vue@next
call npm install --save-dev stylelint stylelint-order
call vagrant up
call vagrant ssh
pause
