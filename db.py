import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

class DsDb():

    def __init__(self,config):

        """
        parses dict of config settings for db connection
        """

        # get credentials for hitting databse
        user    = config['user']
        passwd  = config['passwd']
        host    = config['host']
        db      = config['db']
        port    = config['port']
        flavor  = config['flavor']

        # assemble location string
        location = flavor + '://'
        location += user + ':' + passwd
        location += '@' + host + ':' + str(port) + '/' + db

        # create sqlalchemy objects
        self.engine = create_engine(location)
        self.session = scoped_session(sessionmaker(bind=self.engine))
        self.base = declarative_base()

    def dataframe(self, query):

        """
            returns pandas dataframe from query
        """

        return pd.read_sql(query.statement, self.engine)

    def list_of_lists(self, q):

        df = pd.read_sql(q, self.engine)
        cols = list(df.columns.values)
        data = df.values.tolist()
        r = [cols] + data
        print r
        return r

    def html_table(self,q):
        df = pd.read_sql(q, self.engine)
        return df.to_html(index=False)

    def list_from_query(self,query):

        """
            returns 1-D list for results
        """

        df = self.dataframe(query)
        return list(df[df.columns[0]])

    def value_from_query(self,query):

        """
            returns single value from query
        """

        df = self.dataframe(query)
        try:
            return list(df[df.columns[0]])[0]
        except Exception, e:
            print query.statement
            print e
            return None

    def df_to_sql(self, df, table):

        """
            appends dataframe to existing table
        """

        df.to_sql(
                table,
                self.engine,
                if_exists='append',
                index=False
                )

    def df(self,q):
        df = pd.read_sql(q, self.engine)
        return df


    def val(self,q):
        df = self.df(q)
        try:
            return list(df[df.columns[0]])[0]
        except Exception, e:
            print query.statement
            print e
            return None








