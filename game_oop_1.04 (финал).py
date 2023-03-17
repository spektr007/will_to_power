# 1. Властный. Всегда вступает в борьбу за власть.
class Power:
	def __init__(self):
		self.state = True

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		return self.state

# 2. Альтруист. Никогда не вступает в борьбу за власть.
class Unpower:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		return self.state

# 3. Невластолюбивый имитатор. Начинает с не вступления в борьбу, после чего повторяют предыдущий ход другого игрока.
class Unpower_Imitator:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num != 1:
			self.state = prev_move
		return self.state

# 4. Властолюбивый имитатор. Начинает с борьбы за власть, а далее отвечает одинаково на ход.
class Power_Imitator:
	def __init__(self):
		self.state = True

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num != 1:
			self.state = prev_move
		return self.state

# 5. Властолюбивый инвертор. Начинает с вступления в борьбу за власть, далее отвечает обратно на ходы соперника.
class Power_Invertor:
	def __init__(self):
		self.state = True

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num != 1:
			self.state = not prev_move
		return self.state

# 6. Невластолюбивый инвертор. Начинает с отказа от борьбы за власть, далее отвечает обратно на ходы соперника.
class Unpower_Invertor:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num != 1:
			self.state = not prev_move
		return self.state

# 7. Мстительный. Начинает с отказа от борьбы за власть, пока его не обманут, далее борется за власть до конца.
class Revenge:
	def __init__(self):
		self.state = False
	
	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num != 1 and lied == True:
			self.state = True
		return self.state

# 8. Детектив. Первые четыре хода: не вступать, вступать, не вступать, вступать. Далее, если оппонент ни разу не вступил в борьбу, детектив будет вступать, а в обратном случае – действует как имитатор.
class Detective:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num == 1 or turn_num == 3:
			self.state = False
		if turn_num == 2 or turn_num == 4:
			self.state = True
		if turn_num > 4:
			if prev_move == False:
				self.state = True
			else:
				self.state = prev_move
		return self.state

# 9. Невластолюбивый хитрый имитатор. Первые четыре хода: не вступать, вступать, не вступать, вступать; далее повторяет ходы соперника.
class Unpower_Tricky_Tnvertor:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num == 1 or turn_num == 3:
			self.state = False
		if turn_num == 2 or turn_num == 4:
			self.state = True
		if turn_num > 4:
			self.state = not prev_move
		return self.state

# 10. Властолюбивый хитрый имитатор: Начинает так: вступать, не вступать, вступать, не вступать. Далее повторяет ходы соперника.
class Power_Tricky_Imitator:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num == 1 or turn_num == 3:
			self.state = True
		if turn_num == 2 or turn_num == 4:
			self.state = False
		if turn_num > 4:
			self.state = prev_move
		return self.state

# 11. Властолюбивый хитрый инвентор: Начинает так: вступать, не вступать, вступать, не вступать. Далее отвечает обратно на ходы соперника.
class Power_Tricky_Invertor:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num == 1 or turn_num == 3:
			self.state = True
		if turn_num == 2 or turn_num == 4:
			self.state = False
		if turn_num > 4:
			self.state = not prev_move
		return self.state

# 12. Невластолюбивый хитрый инвентор: Начинает так: не вступать, вступать, не вступать, вступать. Далее отвечает обратно на ходы соперника.
class Unpower_Tricky_Invertor:
	def __init__(self):
		self.state = False

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if turn_num == 1 or turn_num == 3:
			self.state = False
		if turn_num == 2 or turn_num == 4:
			self.state = True
		if turn_num > 4:
			self.state = not prev_move
		return self.state

# 13. Властолюбивый обучающийся инвертор: Сначала вступает в борьбу, потом поступает обратно противнику, если не начинает проигрывать (не равно, а строго меньше) в общем счете. Если же начинает проигрывать, то всегда вступает в борьбу..
class Power_Teaching_Invertor:
	def __init__(self):
		self.state = True

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if score < enemy_score:
			self.state = True
		elif turn_num != 1:
			self.state = not prev_move
		return self.state

# 14. Властолюбивый обучающийся имитатор: Сначала вступает в борьбу, потом поступает как противник, если не начинает проигрывать (не равно, а строго меньше) в общем счете. Если же начинает, то всегда вступает в борьбу.
class Power_Teaching_Imitator:
	def __init__(self):
		self.state = True

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if score < enemy_score:
			self.state = True
		elif turn_num != 1:
			self.state = prev_move
		return self.state

# 15. Властолюбивый обучающийся обманщик и инвертор: Сначала вступает в борьбу, потом поступает обратно противнику, если его не обманут. Потом всегда вступает.
class Power_Teaching_Lier_Invertor:
	def __init__(self):
		self.state = True

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if lied == True:
			self.state = True
		elif turn_num != 1:
			self.state = not prev_move
		return self.state

# 16. Властолюбивый обучающийся обманщик и имитатор: Сначала вступает в борьбу, потом поступает как противник, если его не обманут. Потом всегда вступает.
class Power_Teaching_Lier_Imitator:
	def __init__(self):
		self.state = True

	def move(self, prev_move, turn_num, lied, score, enemy_score):
		if lied == True:
			self.state = True
		elif turn_num != 1:
			self.state = prev_move
		return self.state

import random

# Ниже надо написать номера выбранных алгоритмов.
a = 15
b = 16

# Диапазон вероятностей в процентах для выдачи неправильного ответа первого алгоритма. c <= d. Для правильного ответа ставить 0.
c = 100
d = 100

# Диапазон вероятностей в процентах для выдачи неправильного ответа второго алгоритма. e <= f. Для правильного ответа ставить 0.
e = 100
f = 100

objects = {1: Power(), 2: Unpower(), 3: Unpower_Imitator(), 4: Power_Imitator(), 5: Power_Invertor(), 6: Unpower_Invertor(), 7: Revenge(), 8: Detective(), 9: Unpower_Tricky_Tnvertor(), 10: Power_Tricky_Imitator(), 11: Power_Tricky_Invertor(), 12: Unpower_Tricky_Invertor(), 13: Power_Teaching_Invertor(), 14: Power_Teaching_Imitator(), 15: Power_Teaching_Lier_Invertor(), 16: Power_Teaching_Lier_Imitator()}

player1 = objects[a]
player2 = objects[b]

turn_num = 0

p1_prev_move = player1.state
p1_lied = False
p1_lied_turn = False
p1_score = 0

p2_prev_move = player2.state
p2_lied = False
p2_lied_turn = False
p2_score = 0

for i in range(10): # В скобках указывается количество ходов в раунде.
	
	turn_num += 1
	
	if turn_num == 1:
		p1_real_move = player1.move(player1.state, turn_num, p2_lied, p1_score, p2_score)
	else: 
		p1_real_move = player1.move(p2_prev_move, turn_num, p2_lied, p1_score, p2_score)
	if random.randint(1, 100) > (100 - random.randint(c, d)):
		p1_prev_move = not p1_real_move
		p1_lied = True
		p1_lied_turn = True
	else: 
		p1_prev_move = p1_real_move
		p1_lied_turn = False

	if turn_num == 1:
		p2_real_move = player2.move(player2.state, turn_num, p1_lied, p2_score, p1_score)
	else: 
		p2_real_move = player2.move(p1_prev_move, turn_num, p1_lied, p2_score, p1_score)
	if random.randint(1, 100) > (100 - random.randint(e, f)): 
		p2_prev_move = not p2_real_move
		p2_lied = True
		p2_lied_turn = True
	else:
		p2_prev_move = p2_real_move
		p2_lied_turn = False

# Правила подсчета очков: Оба вступают - каждому по +5 очков. Один вступает, второй нет - первому +5, второму 0. Оба не вступают - каждому по 0. За успешный обман +5.
	if p1_lied_turn == True:
		p1_score += 5
	if p2_lied_turn == True:
		p2_score += 5

	if p1_real_move == p2_real_move and p1_real_move == True:
		p1_score += 5
		p2_score += 5
	elif p1_real_move == p2_real_move and p1_real_move == False:
		p1_score += 0
		p2_score += 0
	elif p1_real_move > p2_real_move:
		p1_score += 5
		# p2_score -= 0
	elif p1_real_move < p2_real_move:
		# p1_score -= 0
		p2_score += 5

	if p1_lied_turn == True and p2_lied_turn == False:
		print(f"Ход {turn_num}, ", end = "")
		print(f"{player1.__class__.__name__} обманул, статус {player1.state}, счет {p1_score}", end = "\t\t")
		print(f"{player2.__class__.__name__},         статус {player2.state}, счет {p2_score}")
	elif p1_lied_turn == False and p2_lied_turn == True:
		print(f"Ход {turn_num}, ", end = "")
		print(f"{player1.__class__.__name__},         статус {player1.state}, счет {p1_score}", end = "\t\t")
		print(f"{player2.__class__.__name__} обманул, статус {player2.state}, счет {p2_score}")
	elif p1_lied_turn == True and p2_lied_turn == True:
		print(f"Ход {turn_num}, ", end = "")
		print(f"{player1.__class__.__name__} обманул, статус {player1.state}, счет {p1_score}", end = "\t\t")
		print(f"{player2.__class__.__name__} обманул, статус {player2.state}, счет {p2_score}")
	else:
		print(f"Ход {turn_num}, ", end = "")
		print(f"{player1.__class__.__name__},         статус {player1.state}, счет {p1_score}", end = "\t\t")
		print(f"{player2.__class__.__name__},         статус {player2.state}, счет {p2_score}")

if p1_score > p2_score:
	print(f"{player1.__class__.__name__} выиграл")
elif p1_score < p2_score:
	print(f"{player2.__class__.__name__} выиграл")
else: 
	print("Ничья")
