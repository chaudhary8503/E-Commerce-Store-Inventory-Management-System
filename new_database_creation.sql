
CREATE TABLE customerDetails
( 
customerID int IDENTITY(1,1) PRIMARY KEY,
customerName varchar(255) NOT NULL,
customerPhoneNumber int NOT NULL,
customerAddress varchar(255) NOT NULL,
customerEmail varchar(255) NULL,
)

CREATE TABLE supplierDetails(
supplierID int IDENTITY(1,1) PRIMARY KEY,
supplierName varchar(255) NOT NULL,
supplierCity varchar(255) NOT NULL,
supplierCountry varchar(255),
supplierEmail varchar(255) NULL,
supplierNumber varchar(255) NOT NULL,
)

CREATE TABLE items(
itemID int PRIMARY KEY,
itemName varchar(255),
itemColour varchar(255),
itemQtyAvailable int,
pricePerUnit float,
)

CREATE TABLE orders(
orderNumber int IDENTITY(1,1) PRIMARY KEY,
customerID int,
orderStatus varchar(50) CHECK (orderStatus IN ('Processing','Dispatched','Delivered','Canceled','Returned')),
orderDate DATE,
orderAmount float,
FOREIGN KEY (customerID) references customerDetails(customerID)
)

CREATE TABLE itemOrder(
orderNumber int ,
itemID int,
pricePerUnit int,
itemQtyBought int,
FOREIGN KEY (orderNumber) references orders(orderNumber),
FOREIGN KEY (itemID) REFERENCES items(itemID),
)


CREATE TABLE purchaseOrder(
purchaseOrderNumber int IDENTITY(1,1) PRIMARY KEY,
supplierID int,
amountPaid int,
dateOfPurchase date,
FOREIGN KEY (supplierID) REFERENCES supplierDetails(supplierID),
) 

CREATE TABLE purchaseItem(
purchaseOrderNumber int,
itemID int,
itemQtyProcured int NOT NULL,
itemCost float,
FOREIGN KEY(itemID) REFERENCES items(itemID),
FOREIGN KEY (purchaseOrderNumber) REFERENCES purchaseOrder(purchaseOrderNumber),
)



/* inserting tumblers*/
INSERT INTO items(itemID,itemName,itemColour,itemQtyAvailable,pricePerUnit)
VALUES (101,'Tumbler','Blue Ombre',5,3200),
		(102,'Tumbler','Silver',5,3200),
		(103,'Tumbler','Coral',5,3200),
		(104,'Tumbler','Candy',5,3200)

/*inserting bottles*/
INSERT INTO items(itemID,itemName,itemColour,itemQtyAvailable,pricePerUnit)
VALUES (201,'Metallic Bottle','Prussian Blue',4,2750),
		(202,'Metallic Bottle','Salmon',5,2750),
		(203,'Metallic Bottle','Sage',7,2750),
		(204,'Metallic Bottle','Crimson',5,2750)

/*inserting metallic straw*/
INSERT INTO items(itemID,itemName,itemColour,itemQtyAvailable,pricePerUnit)
VALUES (301,'Metallic Straw','Rose',12,490),
		(302,'Metallic Straw','Inkey',8,490),
		(303,'Metallic Straw','Holographic',11,490),
		(304,'Metallic Straw','Gold',12,490)

/*inserting tote bags*/
INSERT INTO items(itemID,itemName,itemColour,itemQtyAvailable,pricePerUnit)
VALUES (401,'Tote Bags','Silently Judging',13,450),
		(402,'Tote Bags','Everyday Essentials',8,450)

/*inserting glass tumbler*/
INSERT INTO items(itemID,itemName,itemColour,itemQtyAvailable,pricePerUnit)
VALUES (501,'Glass Tumbler','Transparent',4,1750)

ALTER TABLE customerDetails
ALTER COLUMN customerPhoneNumber VARCHAR(100); 

--INSERTING CUSTOMERS DATA

INSERT INTO customerDetails(customerName,customerPhoneNumber,customerAddress,customerEmail)
VALUES ('Ansab Chaudhary','03008290655','34E 13th Street','ansabchaudhary8@gmail.com'),
		('Ahmad Humayun','03336753188','House 12, Main Khyaban e Hafiz','mh08072@st.habib.edu.pk')

INSERT INTO customerDetails(customerName, customerPhoneNumber, customerAddress, customerEmail)
VALUES
    ('Alice Johnson', '1234567891', '123 Main St', 'alice@gmail.com'),
    ('Bob Smith', '9876543210', '456 Oak St', 'bob@gmail.com'),
    ('Eva Brown', '5551234567', '789 Elm St', 'eva@yahoo.com'),
    ('David Miller', '9871234567', '111 Pine St', 'david@outlook.com'),
    ('Sophie Williams', '7778889999', '222 Cedar St', 'sophie@gmail.com'),
    ('Jack Wilson', '3334445555', '333 Walnut St', 'jack@outlook.com'),
    ('Lily Davis', '1112223333', '444 Maple St', 'lily@yahoo.com'),
    ('Oliver Taylor', '6667778888', '555 Birch St', 'oliver@gmail.com'),
    ('Mia Anderson', '9998887777', '666 Spruce St', 'mia@gmail.com'),
    ('Henry Martinez', '4445556666', '777 Oak St', 'henry@yahoo.com');


--INSERTING SUPPLIER DETAILS
INSERT INTO supplierDetails(supplierName,supplierCity,supplierCountry,supplierEmail,supplierNumber)
VALUES ('Muhammad Ali','Karachi','Pakistan','ali123@gmail.com','03001234567'),
		('Vivi Chan','Beijing','China','vivechan@gmail.com','86-10-1100-2000')


-- 3 rows for China
INSERT INTO supplierDetails (supplierName, supplierCity, supplierCountry, supplierEmail, supplierNumber)
VALUES ('Zhang Wei', 'Beijing', 'China', 'zhangwei@gmail.com', '+8612345678910'),
       ('Li Na', 'Shanghai', 'China', 'li_naB@gmail.com', '+8623456789012'),
       ('Wang Tao', 'Guangzhou', 'China', 'wangtao@gmail.com', '+8634567890123');

-- 2 rows for Pakistan
INSERT INTO supplierDetails (supplierName, supplierCity, supplierCountry, supplierEmail, supplierNumber)
VALUES ('Hamza Khan', 'Lahore', 'Pakistan', 'hamza8@outlook.com', '+924321234567'),
       ('Umar Sohail', 'Karachi', 'Pakistan', 'umarsh@gmail.com', '+922134567890');


insert into orders(customerID,orderStatus,orderDate,orderAmount)
values (2,'Processing','2023/08/01',5000)


insert into itemOrder(orderNumber,itemID,pricePerUnit,itemQtyBought)
values (2,103,3200,2),
		(2,101,3200,3),
		(2,201,1000,1);


insert into purchaseOrder (supplierID,amountPaid,dateOfPurchase)
values (3,10000,'2023/08/01')

insert into purchaseItem(purchaseOrderNumber,itemID,itemQtyProcured)
values (1,101,10),
	(1,103,3)

ALTER TABLE itemOrder
add itemName varchar(255)

ALTER TABLE itemOrder
add itemColour varchar(255)

select * from items
select * from supplierDetails
select * from customerDetails
select * from orders
select * from purchaseOrder
select * from purchaseItem
select * from itemOrder

/*
select sum(pricePerUnit*itemQtyBought)
from itemOrder
group by orderNumber

select C.customerID,C.customerName,count(orderNumber) from orders O join customerDetails C
on O.customerID=C.customerID
group by C.customerID,C.customerName

select sum(orderAmount) from orders where year(orderDate) = 2000

select itemID,count(itemQtyBought) from itemOrder group by itemID

select * from purchaseItem*/