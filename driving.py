driving = input('您是否有駕照?')
if driving != '有' and driving != '沒有':
	print('只能輸入有/沒有')
raise SystemExit 
age = input('您的年齡為:')
if driving == '有':
	if int(age) >= 18:
		print('您通過測驗')
	else:
		print('您已違法!')
elif driving == '沒有':
	if int(age) >= 18:
		print('您可以去考駕照')
	else:
		print('您已通過測驗')
