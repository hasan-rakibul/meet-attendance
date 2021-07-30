import re, pyperclip
from csv import DictWriter
import pandas as pd

course_code, date=input("Enter Course Code <space> Date (e.g. 365 3Jul)\n\n").split()
s=pyperclip.paste()      #collect data from clipboard. So, copy (CTRL C) the whole response before running this code
IDNo=re.compile(r'\d\d\d\d\d\d\d\d')
IDs=IDNo.findall(s)

IDs=list(map(int,IDs))  #IDs were all strings, converting to int to consider as number in excel

# print(IDs)

IDs_df=pd.DataFrame(data=IDs,columns=['ID'])

# IDs_df.to_csv(f'{course_code}_Attendance_Summer21.csv', index=False, columns=[date],mode='a')

# writer = pd.ExcelWriter('400_Attendance_Summer21.xlsx',engine='xlsxwriter')   
# workbook=writer.book
# worksheet=workbook.add_worksheet('ID') 
# writer.sheets['ID']=worksheet
# IDs_df.to_excel(writer,sheet_name='ID',startrow=0 , startcol=0)


with pd.ExcelWriter('/home/rakibul/WORK/BracU/Attendance/All_Attendance_Summer21.xlsx',mode='a',engine='openpyxl') as writer:
    IDs_df.to_excel(writer,sheet_name=f'{course_code}_{date}',index=False)

#with open(f'{course_code}_Attendance_Summer21.csv','a',newline='') as wf:
#    csv_writer = DictWriter(wf,fieldnames = [date])
#    csv_writer.writeheader()
#    for i in ids:
#        csv_writer.writerow({date:i})
