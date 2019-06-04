{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python intro for Network Engineers\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Version: 0.01 <br>\n",
    "Date: 01 May 2019 <br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Install"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For purpose of this tutorial use below\n",
    "- Install Anaconda python\n",
    "- use Python 3.6 or above\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Variables\n",
    "\n",
    "- int\n",
    "- float\n",
    "- string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Variable\n",
    "x = 2\n",
    "y = 5\n",
    "stm = 'Hey'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x+y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'HeyHeyHeyHeyHeyHeyHey'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stm * 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Input/Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is Joe\n"
     ]
    }
   ],
   "source": [
    "print(\"this is Joe\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List, Tuples, Sets and Dictionary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Lists\n",
    "- more like array\n",
    "- ordered list\n",
    "- need to use [] for dening list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "alist = [11, 22, 33, 44, 55]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "22\n",
      "33\n",
      "44\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "for i in alist:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[11, 22, 33, 44, 55, 66]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# add item to list\n",
    "alist.append(66)\n",
    "alist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[11, 22, 44, 55, 66]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# remove item by index\n",
    "alist.pop(2) #index starts from 0 so removeing the thrid item 33\n",
    "alist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[11, 22, 44, 66]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# remove item by value\n",
    "alist.remove(55)\n",
    "alist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[11, 22, 44, 66, 77, 88]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# combine list using extend\n",
    "blist = [77, 88]\n",
    "\n",
    "alist.extend(blist)\n",
    "alist\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 a\n",
      "2 b\n",
      "3 c\n",
      "4 d\n"
     ]
    }
   ],
   "source": [
    "# zip to get x,y values sequentially from two lists\n",
    "\n",
    "x = [1, 2, 3, 4]\n",
    "y = ['a', 'b', 'c', 'd']\n",
    "\n",
    "for i,j in zip(x,y):\n",
    "    print(i,j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ab = zip(x,y)\n",
    "list(ab)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Tuples\n",
    "\n",
    "- Tuples are immutable lists; meaning the values cannot be changed after creation.\n",
    "- Generally used for the grouping information related to same item\n",
    "- Due to immutable nature, below are some use cases\n",
    "    - Tuples heavily used in parallel computing since we can provide the copy fot he input data for each computing node.\n",
    "    - Tuples can be used a Dictionary keys\n",
    "- need to use () for defining tuples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('John', 'Male', 31, 182)"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup1 = ('John', 'Male', 31, 182)\n",
    "tup1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "name, sex, age, height = tup1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John Male 31 182\n"
     ]
    }
   ],
   "source": [
    "print(name, sex, age, height)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Strings "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# String inbuilt functions\n",
    "\n",
    "astring = \"    !!! This is BAD space !!! \""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    !!! This is BAD space !!! \n",
      "    !!! THIS IS BAD SPACE !!! \n",
      "    !!! this is bad space !!! \n"
     ]
    }
   ],
   "source": [
    "print(astring)\n",
    "print(astring.upper())\n",
    "print(astring.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'!!! This is BAD space !!!'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# remove start and tailing space\n",
    "astring.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' remove stra '"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# strip any caracter from string\n",
    "bstring = \"*** remove stra ***\"\n",
    "bstring.strip('*')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['This', 'is', 'Spider', 'man']"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# split string\n",
    "\n",
    "cstring = \"This is Spider man\"\n",
    "cstring.split(' ') # you can use any caracter for split. Comma is mostly used for CSV data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Everyboy in Australia loves oranges.'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# string formating\n",
    "str1 = \"Everyboy in {} loves {}.\"\n",
    "str1.format('Australia', 'oranges')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'man' in cstring "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# partial string check\n",
    "\n",
    "'Spi' in cstring"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dictionary\n",
    "- Dictionary has key value pairs\n",
    "- they are unordered\n",
    "- need to use {} for defining dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1 = {'Name': 'John', 'Age':31, 'Sex': 'Male', 'Height': 182 }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Name': 'John', 'Age': 31, 'Sex': 'Male', 'Height': 182}"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name\n",
      "Age\n",
      "Sex\n",
      "Height\n"
     ]
    }
   ],
   "source": [
    "for i in dict1:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name  is  John\n",
      "Age  is  31\n",
      "Sex  is  Male\n",
      "Height  is  182\n"
     ]
    }
   ],
   "source": [
    "for key, value in dict1.items():\n",
    "    print(key, ' is ', value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### List comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listcomp02 = [i**2 for i in range(1,11)]\n",
    "listcomp02"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5]"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x for x in range(0,6)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 0, 1, 2, 3, 5, 4, 0, 5, 4]"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import random\n",
    "[random.randint(0,i) for i in range(0,10)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create dictionary from dictrionary coprehension\n",
    "\n",
    "{i: i**2 for i in range(1,11)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{0: 4, 1: 16, 4: 81, 2: 49, 6: 64}"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "{random.randint(0,i): i**2 for i in range(0,10)}\n",
    "\n",
    "# the lengh is less than the above example because the keys should be unique. in the previous example\n",
    "# due randomness the keys can be generated in repetion which are ignored. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Sets\n",
    "- unique items\n",
    "- unorded\n",
    "- can do set operations\n",
    "- use set() to create set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Control Flow"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Practice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipaddress\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The ipadress module has below functions\n",
    "- IP address\n",
    "    -  ipaddress.ip_address(address)\n",
    "- networks\n",
    "    -  ipaddress.ip_network(address, strict=True)\n",
    "- interfaces\n",
    "    -  ipaddress.ip_interface(address)\n",
    "\n",
    "More info in python docs [IP address module](https://docs.python.org/3/library/ipaddress.html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "s_ip = ipaddress.ip_address('192.168.1.23')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s_ip.max_prefixlen"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "n_ip = ipaddress.ip_network('192.168.2.0/23')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "IPv4Address('255.255.254.0')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n_ip.netmask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "IPv4Address('0.0.1.255')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# wildcard mask\n",
    "n_ip.hostmask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "192.168.2.1\n",
      "192.168.2.2\n",
      "192.168.2.3\n",
      "192.168.2.4\n",
      "192.168.2.5\n",
      "192.168.2.6\n",
      "192.168.2.7\n",
      "192.168.2.8\n",
      "192.168.2.9\n",
      "192.168.2.10\n",
      "192.168.2.11\n",
      "192.168.2.12\n",
      "192.168.2.13\n",
      "192.168.2.14\n",
      "192.168.2.15\n",
      "192.168.2.16\n",
      "192.168.2.17\n",
      "192.168.2.18\n",
      "192.168.2.19\n",
      "192.168.2.20\n",
      "192.168.2.21\n",
      "192.168.2.22\n",
      "192.168.2.23\n",
      "192.168.2.24\n",
      "192.168.2.25\n",
      "192.168.2.26\n",
      "192.168.2.27\n",
      "192.168.2.28\n",
      "192.168.2.29\n",
      "192.168.2.30\n",
      "192.168.2.31\n",
      "192.168.2.32\n",
      "192.168.2.33\n",
      "192.168.2.34\n",
      "192.168.2.35\n",
      "192.168.2.36\n",
      "192.168.2.37\n",
      "192.168.2.38\n",
      "192.168.2.39\n",
      "192.168.2.40\n",
      "192.168.2.41\n",
      "192.168.2.42\n",
      "192.168.2.43\n",
      "192.168.2.44\n",
      "192.168.2.45\n",
      "192.168.2.46\n",
      "192.168.2.47\n",
      "192.168.2.48\n",
      "192.168.2.49\n",
      "192.168.2.50\n",
      "192.168.2.51\n",
      "192.168.2.52\n",
      "192.168.2.53\n",
      "192.168.2.54\n",
      "192.168.2.55\n",
      "192.168.2.56\n",
      "192.168.2.57\n",
      "192.168.2.58\n",
      "192.168.2.59\n",
      "192.168.2.60\n",
      "192.168.2.61\n",
      "192.168.2.62\n",
      "192.168.2.63\n",
      "192.168.2.64\n",
      "192.168.2.65\n",
      "192.168.2.66\n",
      "192.168.2.67\n",
      "192.168.2.68\n",
      "192.168.2.69\n",
      "192.168.2.70\n",
      "192.168.2.71\n",
      "192.168.2.72\n",
      "192.168.2.73\n",
      "192.168.2.74\n",
      "192.168.2.75\n",
      "192.168.2.76\n",
      "192.168.2.77\n",
      "192.168.2.78\n",
      "192.168.2.79\n",
      "192.168.2.80\n",
      "192.168.2.81\n",
      "192.168.2.82\n",
      "192.168.2.83\n",
      "192.168.2.84\n",
      "192.168.2.85\n",
      "192.168.2.86\n",
      "192.168.2.87\n",
      "192.168.2.88\n",
      "192.168.2.89\n",
      "192.168.2.90\n",
      "192.168.2.91\n",
      "192.168.2.92\n",
      "192.168.2.93\n",
      "192.168.2.94\n",
      "192.168.2.95\n",
      "192.168.2.96\n",
      "192.168.2.97\n",
      "192.168.2.98\n",
      "192.168.2.99\n",
      "192.168.2.100\n",
      "192.168.2.101\n",
      "192.168.2.102\n",
      "192.168.2.103\n",
      "192.168.2.104\n",
      "192.168.2.105\n",
      "192.168.2.106\n",
      "192.168.2.107\n",
      "192.168.2.108\n",
      "192.168.2.109\n",
      "192.168.2.110\n",
      "192.168.2.111\n",
      "192.168.2.112\n",
      "192.168.2.113\n",
      "192.168.2.114\n",
      "192.168.2.115\n",
      "192.168.2.116\n",
      "192.168.2.117\n",
      "192.168.2.118\n",
      "192.168.2.119\n",
      "192.168.2.120\n",
      "192.168.2.121\n",
      "192.168.2.122\n",
      "192.168.2.123\n",
      "192.168.2.124\n",
      "192.168.2.125\n",
      "192.168.2.126\n",
      "192.168.2.127\n",
      "192.168.2.128\n",
      "192.168.2.129\n",
      "192.168.2.130\n",
      "192.168.2.131\n",
      "192.168.2.132\n",
      "192.168.2.133\n",
      "192.168.2.134\n",
      "192.168.2.135\n",
      "192.168.2.136\n",
      "192.168.2.137\n",
      "192.168.2.138\n",
      "192.168.2.139\n",
      "192.168.2.140\n",
      "192.168.2.141\n",
      "192.168.2.142\n",
      "192.168.2.143\n",
      "192.168.2.144\n",
      "192.168.2.145\n",
      "192.168.2.146\n",
      "192.168.2.147\n",
      "192.168.2.148\n",
      "192.168.2.149\n",
      "192.168.2.150\n",
      "192.168.2.151\n",
      "192.168.2.152\n",
      "192.168.2.153\n",
      "192.168.2.154\n",
      "192.168.2.155\n",
      "192.168.2.156\n",
      "192.168.2.157\n",
      "192.168.2.158\n",
      "192.168.2.159\n",
      "192.168.2.160\n",
      "192.168.2.161\n",
      "192.168.2.162\n",
      "192.168.2.163\n",
      "192.168.2.164\n",
      "192.168.2.165\n",
      "192.168.2.166\n",
      "192.168.2.167\n",
      "192.168.2.168\n",
      "192.168.2.169\n",
      "192.168.2.170\n",
      "192.168.2.171\n",
      "192.168.2.172\n",
      "192.168.2.173\n",
      "192.168.2.174\n",
      "192.168.2.175\n",
      "192.168.2.176\n",
      "192.168.2.177\n",
      "192.168.2.178\n",
      "192.168.2.179\n",
      "192.168.2.180\n",
      "192.168.2.181\n",
      "192.168.2.182\n",
      "192.168.2.183\n",
      "192.168.2.184\n",
      "192.168.2.185\n",
      "192.168.2.186\n",
      "192.168.2.187\n",
      "192.168.2.188\n",
      "192.168.2.189\n",
      "192.168.2.190\n",
      "192.168.2.191\n",
      "192.168.2.192\n",
      "192.168.2.193\n",
      "192.168.2.194\n",
      "192.168.2.195\n",
      "192.168.2.196\n",
      "192.168.2.197\n",
      "192.168.2.198\n",
      "192.168.2.199\n",
      "192.168.2.200\n",
      "192.168.2.201\n",
      "192.168.2.202\n",
      "192.168.2.203\n",
      "192.168.2.204\n",
      "192.168.2.205\n",
      "192.168.2.206\n",
      "192.168.2.207\n",
      "192.168.2.208\n",
      "192.168.2.209\n",
      "192.168.2.210\n",
      "192.168.2.211\n",
      "192.168.2.212\n",
      "192.168.2.213\n",
      "192.168.2.214\n",
      "192.168.2.215\n",
      "192.168.2.216\n",
      "192.168.2.217\n",
      "192.168.2.218\n",
      "192.168.2.219\n",
      "192.168.2.220\n",
      "192.168.2.221\n",
      "192.168.2.222\n",
      "192.168.2.223\n",
      "192.168.2.224\n",
      "192.168.2.225\n",
      "192.168.2.226\n",
      "192.168.2.227\n",
      "192.168.2.228\n",
      "192.168.2.229\n",
      "192.168.2.230\n",
      "192.168.2.231\n",
      "192.168.2.232\n",
      "192.168.2.233\n",
      "192.168.2.234\n",
      "192.168.2.235\n",
      "192.168.2.236\n",
      "192.168.2.237\n",
      "192.168.2.238\n",
      "192.168.2.239\n",
      "192.168.2.240\n",
      "192.168.2.241\n",
      "192.168.2.242\n",
      "192.168.2.243\n",
      "192.168.2.244\n",
      "192.168.2.245\n",
      "192.168.2.246\n",
      "192.168.2.247\n",
      "192.168.2.248\n",
      "192.168.2.249\n",
      "192.168.2.250\n",
      "192.168.2.251\n",
      "192.168.2.252\n",
      "192.168.2.253\n",
      "192.168.2.254\n",
      "192.168.2.255\n",
      "192.168.3.0\n",
      "192.168.3.1\n",
      "192.168.3.2\n",
      "192.168.3.3\n",
      "192.168.3.4\n",
      "192.168.3.5\n",
      "192.168.3.6\n",
      "192.168.3.7\n",
      "192.168.3.8\n",
      "192.168.3.9\n",
      "192.168.3.10\n",
      "192.168.3.11\n",
      "192.168.3.12\n",
      "192.168.3.13\n",
      "192.168.3.14\n",
      "192.168.3.15\n",
      "192.168.3.16\n",
      "192.168.3.17\n",
      "192.168.3.18\n",
      "192.168.3.19\n",
      "192.168.3.20\n",
      "192.168.3.21\n",
      "192.168.3.22\n",
      "192.168.3.23\n",
      "192.168.3.24\n",
      "192.168.3.25\n",
      "192.168.3.26\n",
      "192.168.3.27\n",
      "192.168.3.28\n",
      "192.168.3.29\n",
      "192.168.3.30\n",
      "192.168.3.31\n",
      "192.168.3.32\n",
      "192.168.3.33\n",
      "192.168.3.34\n",
      "192.168.3.35\n",
      "192.168.3.36\n",
      "192.168.3.37\n",
      "192.168.3.38\n",
      "192.168.3.39\n",
      "192.168.3.40\n",
      "192.168.3.41\n",
      "192.168.3.42\n",
      "192.168.3.43\n",
      "192.168.3.44\n",
      "192.168.3.45\n",
      "192.168.3.46\n",
      "192.168.3.47\n",
      "192.168.3.48\n",
      "192.168.3.49\n",
      "192.168.3.50\n",
      "192.168.3.51\n",
      "192.168.3.52\n",
      "192.168.3.53\n",
      "192.168.3.54\n",
      "192.168.3.55\n",
      "192.168.3.56\n",
      "192.168.3.57\n",
      "192.168.3.58\n",
      "192.168.3.59\n",
      "192.168.3.60\n",
      "192.168.3.61\n",
      "192.168.3.62\n",
      "192.168.3.63\n",
      "192.168.3.64\n",
      "192.168.3.65\n",
      "192.168.3.66\n",
      "192.168.3.67\n",
      "192.168.3.68\n",
      "192.168.3.69\n",
      "192.168.3.70\n",
      "192.168.3.71\n",
      "192.168.3.72\n",
      "192.168.3.73\n",
      "192.168.3.74\n",
      "192.168.3.75\n",
      "192.168.3.76\n",
      "192.168.3.77\n",
      "192.168.3.78\n",
      "192.168.3.79\n",
      "192.168.3.80\n",
      "192.168.3.81\n",
      "192.168.3.82\n",
      "192.168.3.83\n",
      "192.168.3.84\n",
      "192.168.3.85\n",
      "192.168.3.86\n",
      "192.168.3.87\n",
      "192.168.3.88\n",
      "192.168.3.89\n",
      "192.168.3.90\n",
      "192.168.3.91\n",
      "192.168.3.92\n",
      "192.168.3.93\n",
      "192.168.3.94\n",
      "192.168.3.95\n",
      "192.168.3.96\n",
      "192.168.3.97\n",
      "192.168.3.98\n",
      "192.168.3.99\n",
      "192.168.3.100\n",
      "192.168.3.101\n",
      "192.168.3.102\n",
      "192.168.3.103\n",
      "192.168.3.104\n",
      "192.168.3.105\n",
      "192.168.3.106\n",
      "192.168.3.107\n",
      "192.168.3.108\n",
      "192.168.3.109\n",
      "192.168.3.110\n",
      "192.168.3.111\n",
      "192.168.3.112\n",
      "192.168.3.113\n",
      "192.168.3.114\n",
      "192.168.3.115\n",
      "192.168.3.116\n",
      "192.168.3.117\n",
      "192.168.3.118\n",
      "192.168.3.119\n",
      "192.168.3.120\n",
      "192.168.3.121\n",
      "192.168.3.122\n",
      "192.168.3.123\n",
      "192.168.3.124\n",
      "192.168.3.125\n",
      "192.168.3.126\n",
      "192.168.3.127\n",
      "192.168.3.128\n",
      "192.168.3.129\n",
      "192.168.3.130\n",
      "192.168.3.131\n",
      "192.168.3.132\n",
      "192.168.3.133\n",
      "192.168.3.134\n",
      "192.168.3.135\n",
      "192.168.3.136\n",
      "192.168.3.137\n",
      "192.168.3.138\n",
      "192.168.3.139\n",
      "192.168.3.140\n",
      "192.168.3.141\n",
      "192.168.3.142\n",
      "192.168.3.143\n",
      "192.168.3.144\n",
      "192.168.3.145\n",
      "192.168.3.146\n",
      "192.168.3.147\n",
      "192.168.3.148\n",
      "192.168.3.149\n",
      "192.168.3.150\n",
      "192.168.3.151\n",
      "192.168.3.152\n",
      "192.168.3.153\n",
      "192.168.3.154\n",
      "192.168.3.155\n",
      "192.168.3.156\n",
      "192.168.3.157\n",
      "192.168.3.158\n",
      "192.168.3.159\n",
      "192.168.3.160\n",
      "192.168.3.161\n",
      "192.168.3.162\n",
      "192.168.3.163\n",
      "192.168.3.164\n",
      "192.168.3.165\n",
      "192.168.3.166\n",
      "192.168.3.167\n",
      "192.168.3.168\n",
      "192.168.3.169\n",
      "192.168.3.170\n",
      "192.168.3.171\n",
      "192.168.3.172\n",
      "192.168.3.173\n",
      "192.168.3.174\n",
      "192.168.3.175\n",
      "192.168.3.176\n",
      "192.168.3.177\n",
      "192.168.3.178\n",
      "192.168.3.179\n",
      "192.168.3.180\n",
      "192.168.3.181\n",
      "192.168.3.182\n",
      "192.168.3.183\n",
      "192.168.3.184\n",
      "192.168.3.185\n",
      "192.168.3.186\n",
      "192.168.3.187\n",
      "192.168.3.188\n",
      "192.168.3.189\n",
      "192.168.3.190\n",
      "192.168.3.191\n",
      "192.168.3.192\n",
      "192.168.3.193\n",
      "192.168.3.194\n",
      "192.168.3.195\n",
      "192.168.3.196\n",
      "192.168.3.197\n",
      "192.168.3.198\n",
      "192.168.3.199\n",
      "192.168.3.200\n",
      "192.168.3.201\n",
      "192.168.3.202\n",
      "192.168.3.203\n",
      "192.168.3.204\n",
      "192.168.3.205\n",
      "192.168.3.206\n",
      "192.168.3.207\n",
      "192.168.3.208\n",
      "192.168.3.209\n",
      "192.168.3.210\n",
      "192.168.3.211\n",
      "192.168.3.212\n",
      "192.168.3.213\n",
      "192.168.3.214\n",
      "192.168.3.215\n",
      "192.168.3.216\n",
      "192.168.3.217\n",
      "192.168.3.218\n",
      "192.168.3.219\n",
      "192.168.3.220\n",
      "192.168.3.221\n",
      "192.168.3.222\n",
      "192.168.3.223\n",
      "192.168.3.224\n",
      "192.168.3.225\n",
      "192.168.3.226\n",
      "192.168.3.227\n",
      "192.168.3.228\n",
      "192.168.3.229\n",
      "192.168.3.230\n",
      "192.168.3.231\n",
      "192.168.3.232\n",
      "192.168.3.233\n",
      "192.168.3.234\n",
      "192.168.3.235\n",
      "192.168.3.236\n",
      "192.168.3.237\n",
      "192.168.3.238\n",
      "192.168.3.239\n",
      "192.168.3.240\n",
      "192.168.3.241\n",
      "192.168.3.242\n",
      "192.168.3.243\n",
      "192.168.3.244\n",
      "192.168.3.245\n",
      "192.168.3.246\n",
      "192.168.3.247\n",
      "192.168.3.248\n",
      "192.168.3.249\n",
      "192.168.3.250\n",
      "192.168.3.251\n",
      "192.168.3.252\n",
      "192.168.3.253\n",
      "192.168.3.254\n"
     ]
    }
   ],
   "source": [
    "# number of hosts --> returns a iterator\n",
    "for ip in n_ip.hosts():\n",
    "    print(ip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[IPv4Network('192.168.2.0/25'),\n",
       " IPv4Network('192.168.2.128/25'),\n",
       " IPv4Network('192.168.3.0/25'),\n",
       " IPv4Network('192.168.3.128/25')]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(n_ip.subnets(prefixlen_diff=2)) # which is get /25 from /23 here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[IPv4Network('192.168.2.0/25'),\n",
       " IPv4Network('192.168.2.128/25'),\n",
       " IPv4Network('192.168.3.0/25'),\n",
       " IPv4Network('192.168.3.128/25')]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# alternatively\n",
    "list(n_ip.subnets(new_prefix=25)) # which is get /25 from /23 here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "## api"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ideas for the course structure\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Part 1: \n",
    "    - Start with \n",
    "    - Just do the basic python course\n",
    "        - input, output, print\n",
    "        - loops\n",
    "        - functions\n",
    "        \n",
    "    - projects\n",
    "        - print math table\n",
    "        - print echo of works\n",
    "        - print prime numbers upto given N\n",
    "        - find the count of repetitve words in given sentence\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Final Porject:\n",
    "- small to medium which should be finished in less than 10hours\n",
    "    1. Project Brief\n",
    "        - what are you trying to do\n",
    "        - Why are you doing this\n",
    "    2. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Excersices"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 42, 3]\n"
     ]
    }
   ],
   "source": [
    "x = [1, 2, 3]\n",
    "y = x\n",
    "x[1] = 42\n",
    "print (y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " mylist = [6, 8, 12, 13]\n",
    "mylist[3] % mylist[1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('chemistry', 1997, 2000)"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup1 = ('physics', 'chemistry', 1997, 2000, 2001, 1999)\n",
    "\n",
    "tup1[1:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
