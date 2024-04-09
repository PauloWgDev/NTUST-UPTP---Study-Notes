# Why Databases

Data can be:

- Ubiquitous (abundant, global, everywhere)
- Pervasive (unescapable, prevelant, persistent)

Databases are the best way to store and manage data. Databases make data persistent and sharable in a secure way.

## Data vd Information

**Data** consists of raw facts (raw indicates that the facts have not yet been processed to reveal their meaning.
When the data is entered into the form and saved, it is placed in the underlying database as raw data.

**Information** is the result of processing raw data to reveal its meaning. Data processing can 
be as simple as organizing data to reveal patterns or as complex as making forecasts or drawing 
inferences using statistical modeling. To reveal meaning, information requires context.

"Data is the foundation of information, which is the bedrock of knowledge"

Key Points:
-  Data constitutes the building blocks of information.
- Information is produced by processing data.
- Information is used to reveal the meaning of data.
- Accurate, relevant, and timely information is the key to good decision making.
- Good decision making is the key to organizational survival in a global environment.

**Data management** is a discipline that focuses on the proper generation, storage, and retrieval.

#  Introducing the Database

A database is a shared, integrated computer structure that stores a collection of the following:

- **End-user data** that is, raw facts of interest to the end user
- **Metadata**, or data about data, through which the end-user data is integrated and 
managed

A database management system (DBMS) is a collection of programs that manages the 
database structure and controls access to the data stored in the database

### Role and Advantages of DBMS

The DBMS serves as the intermediary between the user and the database. The database structure itself is stored as a collection of files, and the only way to access the data in those files is 
through the DBMS

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/c46715a6-721d-48cf-92ed-bc656df32c61)

DMBS advantages:

- Improved data sharing
- Improved data security
- Better data integration
- Minimized data inconsistency. (Data inconsistency exists when different versions of the 
same data appear in different places)
- Improved data access. (The DBMS makes it possible to produce quick answers to ad hoc 
queries)
- Improved decision making
- Increased end-user productivity

### Types of Databases

#### Classification by number of users:
- Single Database: supports only one user at a time. (ex: desktop database).
- Multiuser Database: supports multiple users at the same time. (If it supports multiple users, but a relatively small number (less than 50) it is called a workgroup database.)

#### Classification by Location:

- Centralized DB: data located at a single site
- Distributed DB: data distributed across several different sites.
- Cloud DB: a database that is created and mantaned using cloud data services.

#### Classification by Type of data stored

In some contexts, such as research environments, a popular way of classifying databases is 
according to the type of data stored in them.

- General-purpose DB: contain a wide variety of data used in multiple disciplines.
- Discipline-specific DB: contain data focused on specific subject areas.

#### Classification by How the DB will be used

- Operational DB: A database that is designed primarly to support a company's day to day operations. Also known as transactional database or production database.
- Analytical DB: focuses primarily on storing historical data and business metrics used exclusively for tactical or strategic decision making.

Typically, analytical databases comprise two main components: a data warehouse and 
an online analytical processing front end. The data warehouse is a specialized database 
that stores data in a format optimized for decision support.
Online analytical processing (OLAP) is a set of tools that work together to provide 
an advanced data analysis environment for retrieving, processing, and modeling data from 
the data warehouse.

#### Classification by degree of which data is structured

- unstructured data: is data that exists in its original (raw) state
- Structured data: is the result of formatting unstructured data to facilitate storage, use, and generation of information
- Semistructured data:  has already been processed to some extent but does not conform to the strict tabular format typical of the relational model.

#### XML Databases

Extensible Markup Language (XML) is a special language used to represent 
and manipulate data elements in a textual format. An XML database supports the storage and 
management of semistructured XML data

#### No SQL DB

The term NoSQL (Not only SQL) is generally used to describe 
a new generation of DBMS that is not based on the traditional relational database model.

# Why Database Design is Important

Database design refers to the activities that focus on the design of the database structure 
that will be used to store and manage end-user data. A database that meets all user requirements does not just happen; its structure must be designed carefully.
Even a good DBMS will perform poorly with a badly designed database.


## Poor DB Design
![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/23d2a211-04fc-4b82-b524-562fbba4ecc5)


## Good DB Design
![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/60118419-2540-4ef2-96d6-3a60d078b9e7)

With the improved structure, you can use simple commands in a standard data manipulation language to do the following:
- Produce an alphabetical listing of employees by last name:
```SQL
SELECT * FROM EMPLOYEE ORDER BY EMPLOYEE_LNAME;
```
- Determine how many employees are certified in Basic Database Manipulation:
```SQL
SELECT COUNT(*)
FROM SKILL JOIN CERTIFIED ON SKILL.SKILL_ID = CERTIFIED.SKILL_ID 
WHERE SKILL_NAME = 'Basic Database Manipulation';
```

# Evolution of File System Data Processing

### Manual File Systems
Historically, data was kept in paper-and-pencil manual systems organized to facilitate the 
expected use of the data. Typically, this was accomplished through a system of file folders 
and filing cabinets

### Computerized File Systems
Initially, the computer files within the file system were similar to the manual files

When business users wanted data from the computerized file, the DP specialist had to 
create programs to retrieve the data from the file(s), manipulate it in whatever manner the 
user had requested, and present it as a printed report.

As more and more computerized files were developed, the problems with this type of file 
system became apparent. The issues centered around having many data files that contained 
related—often overlapping—data with no means of controlling or managing the data consistently across all of the files.

### File System Redux: Modern End-User Productivity Tools

The users’ desire for direct, hands-on access to data helped to fuel the adoption of personal 
computers for business use.
A common misuse of spreadsheets is as a substitute for a database.

### Problems with File System Data Processing

any change to a file structure, no matter how minor, forces modifications in all of 
the programs that use the data in that file. Modifications are likely to produce errors (bugs),
Those limitations, in turn, lead to problems of structural and data dependence. Also Data redundancy.
Also a file system exhibits structural dependence, maning that access to a file is dependent of its structure. Conversely, structural independence exists when you can change the file structure without affecting the application’s ability to access the data.
Data anomalies, Ideally, a field value change should be 
made in only a single place. Data redundancy, however, fosters an abnormal condition by forcing field value changes in many different locations. A data anomaly develops when not all of the required changes in the redundant data are made successfully.

# Database Systems

The problems inherent in file systems make using a database system very desirable

the database system consists of logically related data stored in a single logical data repository

The database’s DBMS, provides numerous advantages over file system management, by making it possible to eliminate most of the file system’s data inconsistency, data anomaly, data dependence, and structural dependence problems.

The DBMS may even be referred to as the database system’s heart. However, just as it takes 
more than a heart to make a human being function, it takes more than a DBMS to make a 
database system function.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/f0ab927f-18f0-4cd0-9318-e24709f0c578)

## DBMS Functions

- Data dictionary management
- Data storage management
- Data transformation and presentation
- Security management.
- Multiuser access control
- Backup and recovery management
- Data integrity management
- Database access languages and application programming interfaces. (query langugage)
- Database communication interfaces. (accepts end-user requests, for example, might provide 
access to the database via the Internet through the use of web browser or  might support application programming interfaces (API) to communicate with various programing languages)

## DB Challenges 

- Increased costs: Database systems require sophisticated hardware and software and highly skilled personnel.
- Management Complexity.
- Maintaining currency.
- Vendor dependence.
- Frequent upgrade/replacement cycles.

# DB career Oportunities

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/7b1b824d-ac96-4a57-98eb-31f9e7a577d0)

// to do: check out the problems of chapter 1




