import pickle

def register():
    try:
        f=open("register_member.dat","wb")
        l1=[]
        nm=input('Enter User Name you want to create: ')
        ps=input('Enter password you want to create: ')
        l=[nm,ps]
        l1.append(l)
        pickle.dump(l1,f)
        print('Member successfully added. Please login again to access the services.')
        f.close()
    
    except FileNotFoundError:
        f=open("register_member.dat","wb")
        nm=input('Enter User Name you want to create: ')
        ps=input('Enter password you want to create: ')
        l=[[nm,ps]]
        pickle.dump(l,f)
        print('Member successfully added. Please login again to access the services.')
        f.close()

def addbook():
    try:
        f=open("Book_details.dat","rb")
        l=pickle.load(f)
        f.close()
        l1=[]
        while True:
            bcode=int(input("Enter book code:"))
            bname=input("Enter the title of the book:")
            bauthor=input("Enter author's name:")
            bprice=int(input("Enter the book price:"))
            k=[bcode,bname,bauthor,bprice]
            l1.append(k)
            print(bname,'successfully added. Thank You')
            for i in l1:
                l.append(i)
            ch=input("Do you want to add more?Y/N:")
            if ch in 'Nn':
                break
        f1=open('Book_details.dat','wb')
        pickle.dump(l,f1)
        f1.close()
    except FileNotFoundError:
        f1=open('Book_details.dat','wb')
        l1=[]
        while True:
            bcode=int(input("Enter book code:"))
            bname=input("Enter the title of the book:")
            bauthor=input("Enter author's name:")
            bprice=int(input("Enter the book price:"))
            k=[bcode,bname,bauthor,bprice]
            l1.append(k)
            print(bname,'successfully added. Thank You')
            ch=input("Do you want to add more?Y/N:")
            if ch in 'Nn':
                break
        pickle.dump(l1,f1)
        f1.close()

def addmember():
    try:
        f=open("Members_details.dat","ab")
        l=pickle.load(f)
        l1=[]
        while True:
           adm=int(input("Enter student admission number:"))
           mname=input("Enter student name:")
           mnumber=int(input("Enter students roll number:"))
           mclass=int(input("Enter student's class:"))
           msection=input("Enter student's section:")
           memail=input("Enter students's email:")
           k=[adm,mname,mnumber,mclass,msection,memail]
           l1.append(k)
           print('\n 1 student successfully added to the list \n')
           ch=input("Do you want to add more?Y/N:")
           if ch in 'Nn':
              break
        for i in l1:
            l.append(i)
        f1=open('Members_details.dat','wb')
        pickle.dump(l,f1)
        f1.close()
    except :
        f1=open('Members_details.dat','wb')
        l1=[]
        while True:
            adm=int(input("Enter student admission number:"))
            mname=input("Enter student name:")
            mnumber=int(input("Enter students roll number:"))
            mclass=int(input("Enter student's class:"))
            msection=input("Enter student's section:")
            memail=input("Enter students's email:")
            k=[adm,mname,mnumber,mclass,msection,memail]
            l1.append(k)
            print('\n 1 student successfully added to the list \n')
            ch=input("Do you want to add more?Y/N:")
            if ch in 'Nn':
                break
        pickle.dump(l1,f1)
        f1.close()
        

def viewmember():
    try:
        f=open("Members_details.dat","rb")
        l=pickle.load(f)
        print('Library Members List','\n')
        for i in l:
           print("Admission number:",i[0])
           print('Student Name: ',i[1])
           print('Class: ',i[3])
           print('Section: ',i[4])
           print('Roll Number: ',i[5])
           print('Email id: ',i[4],'\n')
        f.close()
    except FileNotFoundError:
        print("No existing students. Please add some students first.")
       

def viewbook():
    try:
        f=open("Book_details.dat","rb")
        l=pickle.load(f)
        print('Library Books List','\n')
        for i in l:
            print('Book Name:\t',i[1])
            print('Book Author:\t',i[2])
            print('Book Code:\t',i[0],'\n')
        f.close()
    except FileNotFoundError:
        print("No existing books. Please add some books first.")


def issuebook():
    import datetime
    from datetime import timedelta
    f=open('issue_book.dat','wb')
    l=[]
    admno=int(input("Enter admission number:"))
    f1=open("Members_details.dat",'rb')
    m=pickle.load(f1)
    for i in m:
       if i[0]==admno:
            bid=int(input('Enter book code: '))
            of=open("Book_details.dat","rb")
            p=pickle.load(of)
            for i in p:
                if i[0]==bid:
                    n=datetime.datetime.now()
                    date=n.strftime("%d-%b-%Y")
                    time=n.strftime('%H:%M:%S')
                    dd=n + timedelta(days=7)
                    duedate=dd.strftime('%d-%b-%Y')
                    l1=[admno,bid,duedate]
                    l.append(l1)
                    pickle.dump(l,f)
                    print('The following book has been borrowed on',date,'at',time)
                    print('Student with admission number:\t',admno,'\nhas been issued the book with \nBook id:\t',bid,'\nDue Date:\t',duedate,'\n')
                    print('Please return the book borrowed on or before the due date')
                    f.close()
                    f1=open("book_details.dat","rb")
                    l2=pickle.load(f1)
                    for i in l2:
                        if i[0]==bid:
                            l2.remove(i)
                    f1.close()
                    f2=open("Book_details.dat","wb")
                    pickle.dump(l2,f2)
                    f2.close()
                    ab=open("Members_details.dat","rb")
                    w=pickle.load(ab)
                    for i in w:
                        if i[0]==admno:
                            w.remove(i)
                    ab.close()
                    abc=open("Members_details","wb")
                    pickle.dump(w,abc)
                    abc.close()
                else:
                    print("The following book does not exists. Kindly enter new book.")
       else:
           print("The student name entered does not exist. Kindly enter new student name.")
        


def returnbook():
    from datetime import datetime, timedelta
    f=open('issue_book.dat','rb+')
    l=pickle.load(f)
    print(l)
    admno=int(input("Enter admission number:"))
    bid=int(input('Enter book code: '))
    for i in l:
        if i[0]==admno and i[1]==bid:
            n=datetime.now()
            date=n.strftime("%d-%b-%Y")
            time=n.strftime('%H:%M:%S')
            duedt=datetime.strptime(i[2],"%d-%b-%y")
            if duedt>=n:
                print('The following book has been returned on',date,'at',time)
                print('Student with admission number:\t',admno,'\nBook id:\t',bid,'\nReturned Date:\t',date,'\n')
                print('Thank you for visiting the Library')
            else:
                print('Student with Admission number:\t',admno,'\nhas returned the book of id\n book id:\t',bid,(x-i[2]).days,'late.\nKindly pay the following fine for the same:\t',7*((x-i[2]).days))
            l.remove(i)
            f.seek(0)
            print(l)
            pickle.dump(l,f)
            f.close()
            o=open("book_details.dat",'rb+')
            l=pickle.load(o)
            l.append(i)
            print(l)
            pickle.dump(l,o)
            f.close()
    else:
        print("No such record exists.")

def deletemember():
   f=open("Members_details.dat","rb+")
   m=pickle.load(f)
   a=int(input("Enter admission number:"))
   for i in m:
      if i[0]==a:
         print("Record exists")
         print("Details are:")
         print("Student Name:",i[1])
         print("Student Roll number:",i[2])
         print("Student class:",i[3])
         print("Student section:",i[4])
         print("Student email:",i[5])
         q=input("Do you want to delete?Y/N:")
         if q in 'Yy':
            m.remove(i)
            print("Student removed")
            pickle.dump(m,f)
         else:
             print("Student does not exists")
            
def deletebook():
   f=open("Book_details.dat","rb+")
   m=pickle.load(f)
   a=int(input("Enter book id:"))
   for i in m:
      if i[0]==a:
         print("Record exists")
         print("Details are:")
         print("Book Name:",i[1])
         print("Author Name:",i[2])
         q=input("Do you want to delete?Y/N:")
         if q in 'Yy':
            m.remove(i)
            print("Book removed")
            pickle.dump(m,f)
         else:
             print("Book does not exists")
   


while True:
    print("*"*140)
    print()
    l="Welcome to library"
    print(l.center(220))
    print()
    print("*"*140)
    p="Press:"
    print(p.center(225))
    q="L. To Login"
    print(q.center(225))
    o="R. To Register"
    print(o.center(225))
    s="E. To Exit"
    print(s.center(225))
    qwe=input("Enter your choice:")
    
    if qwe in 'Rr':
        register()
       
    elif qwe in 'Ll':
        try:
            t=input("Enter your username:")
            k=input("Enter your password:")
            f=open("register_member.dat","rb")
            r=pickle.load(f)
            for i in r:
                if i[0].lower()==t.lower() and i[1]==k:
                    while True:
                        print("You can add a book to library, view available books in library, issue books to students and many more....")
                        print()
                        a="Please choose the desired option according to your need"
                        print(a.center(130))
                        print()
                        b="1. Add Book"
                        print(b.center(120))
                        c="2. Add Member"
                        print(c.center(122))
                        d="3. Issue Book"
                        print(d.center(122))
                        e="4. Return Book"
                        print(e.center(122))
                        f="5. View Books"
                        print(f.center(122))
                        g="6. View Members"
                        print(g.center(124))
                        h="7.Delete a member"
                        print(h.center(124))
                        i="8.Delete a book"
                        print(i.center(124))
                        j="9. Exit"
                        print(j.center(116))
                        ch=input("Enter the option number you would like to perform: ")
                        print()
                        if ch=='1':
                            addbook()
                        elif ch=='2':
                            addmember()
                        elif ch=='3':
                            issuebook()
                        elif ch=='4':
                            returnbook()
                        elif ch=='5':
                            viewbook()
                        elif ch=='6':
                            viewmember()
                        elif ch=='7':
                           deletemember()
                        elif ch=='8':
                           deletebook()
                        elif ch=='9':
                            break
                        else:
                            print("Please enter correct number")
                else:
                    print("Please enter correct user/password")
        except FileNotFoundError:
            print('No members added. Please register yourselves first')
    elif qwe in 'Ee':
        break
    else:
        print('Please enter correct symbol')

