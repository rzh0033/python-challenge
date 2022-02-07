{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9de928d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8f1478f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set Path\n",
    "pollCSV = os.path.join('Resources', 'election_data.CSV')\n",
    "pollCSV = r'C:\\Users\\rzh00\\Documents\\gt-virt-atl-data-pt-09-2021-u-c-master\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0f207e3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Varibales\n",
    "candi = []\n",
    "vote_count = []\n",
    "vote_percent = []\n",
    "\n",
    "num_vote = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "08423af7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Open CSV\n",
    "with open(pollCSV) as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = ',')\n",
    "    csvheader = next(csvreader)\n",
    "    for row in csvreader: \n",
    "        num_vote = num_vote + 1 # total votes\n",
    "        candi_name = row[2] # adding candidate name to array\n",
    "        \n",
    "        if candi_name not in candi: #conditional to append any new candidates \n",
    "            candi.append(candi_name)\n",
    "            index = candi.index(row[2])\n",
    "            vote_count.append(1)\n",
    "        else:\n",
    "            index = candi.index(row[2])\n",
    "            vote_count[index] += 1\n",
    "            \n",
    "    for i in vote_count: # find the percentage of the votes recieved\n",
    "        percent = round((i/num_vote) * 100)\n",
    "        percent = '%.3f%%' % percent\n",
    "        vote_percent.append(percent)\n",
    "        \n",
    "    winner = max(vote_count) # determine winner and update the value\n",
    "    index = vote_count.index(winner)\n",
    "    candi_winner = candi[index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "400521a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "--------------------\n",
      "Total Votes[4436463, 1408401, 985880, 211260]\n",
      "--------------------\n",
      "Khan: 63.000% (4436463)\n",
      "Correy: 20.000% (1408401)\n",
      "Li: 14.000% (985880)\n",
      "O'Tooley: 3.000% (211260)\n",
      "--------------------\n",
      "Winning Candidate: 4436463\n"
     ]
    }
   ],
   "source": [
    "#Print Results\n",
    "print('Election Results')\n",
    "print('-' * 20)\n",
    "print(f'Total Votes' + str(vote_count))\n",
    "print('-' * 20)\n",
    "for i in range(len(candi)):\n",
    "    print(f'{candi[i]}: {str(vote_percent[i])} ({str(vote_count[i])})')\n",
    "print('-' * 20)\n",
    "print(f'Winning Candidate: {winner}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "18e81981",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = os.path.join('output', 'result.txt')\n",
    "result = r'C:\\Users\\rzh00\\Documents\\gt-virt-atl-data-pt-09-2021-u-c-master\\02-Homework\\03-Python\\Instructions\\PyPoll\\result.txt'\n",
    "\n",
    "with open(result, 'w') as txt:\n",
    "    txt.write('Election Results')\n",
    "    txt.write('-' * 20)\n",
    "    txt.write(f'Total Votes' + str(vote_count))\n",
    "    txt.write('-' * 20)\n",
    "    for i in range(len(candi)):\n",
    "        txt.write(f'{candi[i]}: {str(vote_percent[i])} ({str(vote_count[i])})')\n",
    "    txt.write('-' * 20)\n",
    "    txt.write(f'Winning Candidate: {winner}')\n",
    "    txt.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5893e30",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
