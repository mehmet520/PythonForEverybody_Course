# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name= input ('Enter file name: \n')
if len(name) < 1 :
    name='mbox-short.txt'
handle=open (name)  # Python liest die Datei.

count_email_messages= {}
for line in handle:
    line=line.rstrip()
    words=line.split ()  # List wurde erstellt. words ['ccc', 'xxx']
    
    if len (words) < 1 or words[0] != 'From': continue
    mail_adress= words [1]  # Erkannte E-Mail-Adressen werden einer Variablen zugewiesen.
    count_email_messages[mail_adress]= count_email_messages.get (mail_adress, 0) + 1    # Worterbuch wird produziert.

# Das Programm liest das Wörterbuch mit einer maximalen Schleife, um den produktivsten Committer zu finden.
hochster_Wert = 0
most_prolific_committer = ' None '
for email, zahl in count_email_messages.items():
    if zahl > hochster_Wert:
        hochster_Wert=zahl
        most_prolific_committer=email

print (most_prolific_committer, hochster_Wert)