# Paddy Product Finder (pp-finder)

This is a first draft at solving a data problem at work. This is my first time using python. This is a quick and dirty solution because we are under time pressure.

## Problem statement
 A supplier will give our purchasing team a list, and they'd like to get the historical sales data for this new list. Problem is that there no code or sku that perfectly aligns with the two lists. This task is currently being performed manually


## Breaking down the problem

I can split this down into 2 main parts: 

	 - Problem 1. How to get the related sales data. So from a list of new season skus, find all relevant and related skus. So a key task for the tool is input a list of skus, output a list of all related skus out (From a list of new/ current season skus from icebreaker)

	 - Problem 2. How to display sales data for aggregated skus (and what kind of data would you like to show? Interactive chart?)

## Breaking this further down and brainstorming
	1. Get a list of current/new skus from icebreaker
	2. Input either a single sku, or a list of skus into a tool/app
	3. Tool does the work of finding all related past skus AND
	4. Tool takes this list of related skus and displays sales data in a useful way 
	5. User is able to interact with sales data (dig in and find which exact skus, remove or add a sku on the fly)

### First attempt 

Reading the excel files were not too tricky. The crux is how to determine if a sku is related or not? I tried to use a fuzzy search but was not happy with results. I didn't look too deep into tweaking fuzzywuzzy. I then stumbled across BERT (A google natural language transformer) and now I am in over my head. With the help of GPT I've got something together. 

One ammendment to problem 1- I only need to find the most related sku instead of many results. 

After reaching out to a community, here are some other things to try:
 - "Another potential strategy is removing common terms/attributes in the equation which typically contribute to false matches particularly if it consumes most of the input presentation like your 'ZoneKnit Leggings' example. "
 - "Try defining match clusters based on the match scores so you can focus on which ones to tweak:

Exact (1) 
Very High (.95-1)
High (.90-.94)
Medium (.85 -.9)
and so on.

Typically you blindfoldedly accept the first two clusters above and safely automate them to your downstream processes

Top tip: about data quality/data matching, you do not draw lines, you draw circles and there will always be those outliers.