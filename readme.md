# cli command

locust -f api_test_sequential.py --headless -u 10 -r 2 --run-time 30s --host https://reqres.in --print-stats --csv ./reports/api_run.csv --csv-full-history
locust -f api_test_sequential.py --headless -u 10 -r 2 --run-time 30s --host https://reqres.in --print-stats --csv ./reports/api_run.csv --csv-full-history -L INFO --logfile ./reports/runlog.log --html ./reports/testreport.html