temperatures=[15,18,12,20,16,14,19,17,13,21,15,16,18,20]
max_temp=max(temperatures)
min_temp=min(temperatures)
avg_temp=sum(temperatures)/len(temperatures)
days_above_avg=len([t for t in temperatures if t>avg_temp])
sorted_temps=sorted(temperatures)
fahrenheit=[t*9/5+32 for t in temperatures]
print(f"Температуры: {temperatures}")
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")
print(f"Средняя: {avg_temp:.1f}°C")
print(f"Дней выше средней: {days_above_avg}")
print(f"Отсортированные: {sorted_temps}")
print(f"Фаренгейты: {fahrenheit}")