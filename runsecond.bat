call cd frontend2
call mkdir dist
call cd dist
call mkdir iview
call xcopy ..\..\iview iview\ /e
call cd ..
call npm install
call npm run dev