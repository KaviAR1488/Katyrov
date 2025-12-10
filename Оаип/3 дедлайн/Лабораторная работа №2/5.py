def filter_logs(log_lst,keyword):
    for log in log_lst:
        if keyword in log:
            yield log