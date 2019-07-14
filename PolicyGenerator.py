# This script will be used to generate multiple 
# policies used for testing.
#
#
#
#
#
#
import random
import json

filename="policy7"
lt_operators = ['<','LT','<=','LE']
gt_operators = ['>','GT','>=','GE']
not_operators = ['!','^','NOT','!=','^=','NE']
eq_operators = ['=','EQ']
and_or_operators = ['IN','|','OR','&&','AND',]
math_opeators = ['+','-','*','/']
concat_operators = ['||','CONCAT']
sysaff_table = ['(\'JES2\')','(\'JESA\')','(\'JESC\')','(\'JESF\')']
actions_table = ['holdJob','modifyJob','cancelJob','purgeOutput']
attribute_table = ['jobname','jobprty','sysaff','jobaffinity','held','substr','match','length']
affinity_values = ['(\'N1M1\')','(\'N1M2\')','(\'N2M1\')','(\'N2M2\')']
alphabet_numbers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
#policy25

def Create_PolicyName(name_len):   #Need to create policy names of varying lengths, all upper, all lower, and mixed case.
	name_case = random.randint(1,3)
	policyName = ""
	if(name_case == 1):
		policyName = All_Upper(name_len)
	if(name_case == 2):
		policyName = All_Lower(name_len)
	if(name_case == 3):
		policyName = Mixed_Case(name_len)
	return policyName
#*********************************************************************
def All_Upper(name_len):
	policyName = ""
	for i in range(name_len):
		policyName += random.choice(alphabet_numbers)
	print(policyName.upper())
	return policyName.upper()
#*********************************************************************
def All_Lower(name_len):
	policyName = ""
	for i in range(name_len):
		policyName += random.choice(alphabet_numbers)
	print(policyName.lower())
	return policyName.lower()
#*********************************************************************
def Mixed_Case(name_len):
	policyName = ""
	newPolicyName = ""
	for i in range(name_len):
		policyName += random.choice(alphabet_numbers)
	for aLetter in policyName:
		determine_case = random.randint(1,2)
		if(aLetter.isalpha() and determine_case == 2):
			newPolicyName += aLetter.upper()
		else:
			newPolicyName += aLetter
	print(newPolicyName)
	return newPolicyName
#*********************************************************************
def Create_Condition(num_conditions=1,condition_names = []):
	condition_string = []
	if len(condition_names) == 0:
		for i in range(num_conditions):
			num_attributes = len(attribute_table) - 1
			attribute_choice = random.choice(attribute_table)
			the_condition = attribute_choice		
			if the_condition == 'jobaffinity':
				affinity_choice = random.choice(affinity_values)
				the_condition += affinity_choice			
			if the_condition == 'sysaff':
				sysaff_choice = random.choice(sysaff_table)
				the_condition += sysaff_choice
			condition_string.append(the_condition)
	else:
		for name in condition_names:
			if name == 'jobaffinity':				
				affinity_choice = random.choice(affinity_values)
				name += affinity_choice
			if name == 'sysaff':
				sysaff_choice = random.choice(sysaff_table)
				name += sysaff_choice
			condition_string.append(name)			
	return condition_string
#*********************************************************************
def Create_Actions(num_actions=1,action_names=[]):
	action_string = []
	if len(action_names) == 0:
		for i in range(num_actions):
			action_choice = random.choice(actions_table)
			action_string.append(action_choice)
	else:
		for name in action_names:
			action_string.append(name)
	return action_string
#*********************************************************************
def Create_Policy(policyName = 'default',policyVersion = 1, policyType = 'default',numConditions = 2,numActions = 2):
	policyString = []
	condition = Create_Condition(numConditions)	
	if policyName == 'default':
		policyName = Create_PolicyName(8)
	if policyType == 'default':
		policyType = 'JobConversion'
	policyString.append('{')
	policyString.append('   "policyName":     "' + policyName + '",')
	policyString.append('   "policyVersion":  ' + str(policyVersion) + ',')
	policyString.append('   "policyType":     "' + policyType + '",')
	policyString.append('   "definitions":')
	policyString.append('     [')
	for i in range(numConditions):	
		policyString.append('       {')
		policyString.append('           "condition" : "' + condition[i] + '",')
		policyString.append('           "actions" :')
		policyString.append('              [')
		for j in range(numActions):
			action = random.choice(actions_table)
			policyString.append('                 {')
			policyString.append('                    "action" : "'+action+'"')
			if numActions > 1 and j < numActions - 1:
				policyString.append('                 },')
			else:
				policyString.append('                 }')
		policyString.append('              ]')
		if numConditions > 1 and i < numConditions - 1:
			policyString.append('       },')
		else:
			policyString.append('       }')
	policyString.append('     ]')
	policyString.append('}')
	my_file = open(filename,"a")
	for x in policyString:
		print(str(x))
		my_file.write('%s \n' %(x))
	return
	my_file.close()

	
Create_Policy()


#All_Upper(50)
#All_Lower(5)
#Mixed_Case(120)
print("**********************************************************")

print(json.dumps({"policyName":"Job1",
                  "policyVersion":1, 
                  "policyType":"JobConversion",
                  "defenitions":
					 [
					   {
					     "condition" : "jobaffinity('N1M1')",
					     "actions" : 
					       [
					         {
					           "action" : "holdJob"
							 },
							 {
                               "action" : "modifyJob",
                               "attribute" : "jobClass",
                               "value" : "D"							   	   
							  }
						   ]
						},
                        {
                          "condition" : " jobaffinity('N1M2') ",
                          "actions" :
                            [
                             {
                               "action" : "cancelJob"
                             },
                             {
                               "action" : "modifyJob",
                               "attribute" : "SYSAFF",
                               "value" : "addlist(setaff, 'N1M3') "
                             }
                            ]
                          }
                       ]							  	   
	             },indent=4))


