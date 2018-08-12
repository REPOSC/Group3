vagrant plugin install vagrant-vbguest
npm install --save-dev mocha
cd frontend
npm install
npm install --save-dev eslint eslint-plugin-vue@next
npm install --save-dev stylelint stylelint-order
cd ../frontend2
npm install
npm install --save-dev eslint eslint-plugin-vue@next
npm install --save-dev stylelint stylelint-order
vagrant up
vagrant ssh
pause
