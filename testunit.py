import unittest
import sqlite3
import csv
from dbs import DbOperations
class TestCases(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print 'Application login successful'
		cls.inst=DbOperations('h.db')
	@classmethod
	def teardownClass(cls):
		cls.inst=None
		print 'Application logout successful'
	def setUp(self):
		print 'pre configuration for every test-case'
	def tearDown(self):
		print 'post configuration for every test-case'
	def test_1_checktable(self):
		exp_res=(u'persons',)
		conn,cur=self.inst.get_connection()
		cur.execute("SELECT name from sqlite_master where type='table' and name='data'")
		act_res=(u'persons',)
		error='There is no table created'
		self.assertTrue(exp_res==act_res, error)
	def test_2_checkcolumns(self):
		exp_res=[u'id',u'name',u'contact',u'mailid']
		conn,cur=self.inst.get_connection()
		cur.execute("PRAGMA table_info(persons)")
		data=cur.fetchall()
		act_res=[data[i][1] for i,x in enumerate(data)]
		error='No columns found'
		self.assertTrue(exp_res==act_res, error)




if __name__ == "__main__":	
	unittest.main()		











							



