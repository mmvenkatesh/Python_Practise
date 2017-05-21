import sqlite3
import logging
import csv
logging.basicConfig(Filename='database.log',level=logging.DEBUG,
	format="%(asctime)s->%(levelname)s->%(message)s")

class DbOperations():

	def __init__(self,dbname):
		self.dbname=dbname

	def get_connection(self):
		try:
		  logging.info('Establishing connection to database')
		  conn=sqlite3.connect(self.dbname)
		  logging.info('connected to database {0}'.format(self.dbname))
		  cur=conn.cursor()
		  return conn,cur
		except Exception as err:
			logging.warn('The error message is {0}'.format(err))

	def create_table(self,query):
		try:
			conn,cur=self.get_connection()
			cur.execute(query)
			conn.commit()
			logging.debug('The table got created with query {0}'.format(query))
			conn.close()
			logging.info('connection to database got closed')
		except Exception as err:
			logging.warn('The error message is {0}'.format(err))

	def insert_values_table(self,query,list2):
		conn,cur=self.get_connection()
		logging.info('connected to the database')
		try:
			for a in list2:
				cur.execute(query,a)
				logging.debug('The value in {0} got inserted in to the table'.format(query))
			conn.commit()
			conn.close()
			logging.info('The connection to database got closed')
		except Exception as err:
			logging.warn('The error message is {0}'.format(err))

	def delete_values_table(self,query):
		conn,cur=self.get_connection()
		try:
			cur.execute(query)
			conn.commit()
			logging.debug('The value in {0} got deleted from table'.format(query))
			conn.close()
			logging.info('The connection to database got closed')
		except Exception as err:
			logging.warn('The error message is {0}'.format(err))   

	def update_values_table(self,query):
		conn,cur=self.get_connection()
		try:
		   cur.execute(query)
		   conn.commit()
		   logging.debug('The table got updated with {0}'.format(query))
		   conn.close()
		   logging.info('The connection to database got closed')
		except Exception as err:
		   logging.warn('The error message is {0}'.format(err))

	def get_values_database(self,query):
		conn,cur=self.get_connection()
		try:
			cur.execute(query)
			logging.debug('Got values for the {0}'.format(query))
			data=cur.fetchall()
			return data
		except Exception as err:
			logging.warn('The eror message is {0}'.format(err))

	def write_data_file(self,query,filename,*args):
		data=self.get_values_database(query)
		logging.info('got data from database')
		try:
			f=open(filename,'wb')
			logging.debug('opening file in debug mode')
			write=csv.writer(f,delimiter=' ',quotechar='|')
			write.writerow(args)
			logging.info('written heading to the file')
			for a in data:
				write.writerow(a)
			logging.debug('copied contents to the file')        
			f.close()
			logging.info('closing the file')
		except Exception as err:
			logging.warn('The error message is {0}'.format(err))
