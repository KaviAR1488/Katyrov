def format_report(report_title:str,*data,**properties):
    """Форматирует отчет с данными и свойствами."""
    print(f"--- Отчет: {report_title} ---")
    print("Данные:")
    for item in data:
        print(f" - {item}")
    print("\nСвойства:")
    for key,value in properties.items():
        print(f" - {key}: {value}")
    print("------------------------------")