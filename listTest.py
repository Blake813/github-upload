import random

empty_list = []
my_list = ['abcd']
lt_operators = ['<','LT','<=','LE']
gt_operators = ['>','GT','>=','GE']
not_operators = ['!','^','NOT','!=','^=','NE']
eq_operators = ['=','EQ']
and_or_operators = ['IN','|','OR','&&','AND',]
math_opeators = ['+','-','*','/']
concat_operators = ['||','CONCAT']
sysaff_table = ['(\'JES2\')','(\'JESA\')','(\'JESC\')','(\'JESF\')']
actions_table = ['"holdJob"','"modifyJob"','"cancelJob"','"purgeOutput"']
attribute_table = ['jobname','jobprty','sysaff','jobaffinity','held','substr','match']
affinity_values = ['(\'N1M1\')','(\'N1M2\')','(\'N2M1\')','(\'N2M2\')']
alphabet_numbers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

def Print_List(a_list):
	print(len(a_list))
	for x in a_list:
		print(x)
	return

def Create_Actions(num_actions=1,action_names=[]):
	action_string = []
	if len(action_names) == 0:
		for i in range(num_actions):
			total_actions = len(actions_table) - 1
			action_choice = random.randint(1,total_actions)
			action_name = actions_table[action_choice]
			action_string.append(action_name)
	else:
		for name in action_names:
			action_string.append(name)
	return action_string

#Print_List(empty_list)
