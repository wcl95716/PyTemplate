


from custom_services.tianyi.server.wx_task import task_creat

def creat_notification_tasks(vehicle_url: str, rule_url: str) -> None:
    task_creat(vehicle_url, rule_url)
    pass 

