#!/usr/bin/python
#Post length and average answer length Exercise

import sys
import csv
import string

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

#creates empty global variables for the output we eventually get
question={}
answer={}
lenList=[]

#goes through each line of the code
for line in reader:
    #line[5] is the node type ("question", "answer", or "comment") in our dataset
	node_type=line[5]
	#line[4] is the body of the text; we want its length
	body=line[4]
	body_len=len(body)
	#line[0] is the node id
	node_id=line[0]
	question_id=str(line[7])
	
	#if the post is a question, save in the question dictionary, key=node_id,value=question length
	if node_type=="question":
		question[node_id]=body_len
	
	#if the post is an answer, save in the answer dictionary, key=question id,value=answer length
	if node_type=="answer":
		if not question_id in answer:
			answer[question_id]=[body_len]
		else:
			answer[question_id].append(body_len)
			

#print out the answer length for each question, if the question has no answer, print 0 as the answer length
for id in question:
	if not id in answer:
		print "{0}\t{1}\t{2}".format(int(id),int(question[id]),"0")
	else:
		for length in answer[id]:
			print "{0}\t{1}\t{2}".format(int(id),int(question[id]),length)