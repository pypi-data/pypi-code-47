from webgatewayapi.authenticate import authenticate
from webgatewayapi.parse import parseData
from webgatewayapi.process import process

class listdata(object):
    """
        lisdata class object will create list APIs, it is depended on process class object to process data. Any
        list api operations must be created here. For initialize auth, hostname are required.
        :return list specific API methods.
    """
    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https


    def listData(self, pagesize=100, page=1):
        """
        listData will pull all the lists based on the listID, depending on the size of lists pagesize is used to
        iterate through all pages.
        :param pagesize:  Max Page Size
        :param page: initial page
        :return: All lists based on the pagesize..
        """

        r = self.auth.get(self.listURL(), params={'pageSize': pagesize})
        p = process(data=parseData(r.text))
        data = p.processList()
        pages = p.processPages()
        if len(pages) is not 1:
            data = [data]
            for page in pages:
                r = self.auth.get(self.listURL(), params={'pageSize': pagesize, 'page': page})
                p = process(data=parseData(r.text))
                data.append(p.processList())
            p = process(data=data)
            data = p.processListCombine()
        return data



    def listID(self, value):
        """
            listID will generate specific list details from the server.
        :param value: listID of the list
        :return: full list information.
        """
        r = self.auth.get(self.listURL(value=value))
        p = process(data=parseData(r.text))
        return p.processListID()



    def listEntryInsertModify(self, value, entry, description, position=1, insert=None):
        """
            listIDInsert will insert a list entry with value, description at the position:1 unless specified.
        :param value: listID
        :param entry: List Entry
        :param description: List Description
        :param position: List Entry Position.
        :return: Status response of the post.
        """
        i = '''<entry xmlns="http://www.w3org/2011/Atom">
                    <content type="application/xml">
                        <listEntry>
                            <entry>{}</entry>
                            <description>{}</description>
                        </listEntry>
                    </content> 
                </entry>'''
        if insert == "insert":
            u = self.listURL(value=value, entry=position, insert=insert)
            i = i.format(entry, description)
            r = self.auth.post(u, data=i, headers={'Content-Type': 'application/xml'})
            return parseData(r.text)
        else:
            u = self.listURL(value=value, entry=position)
            i = i.format(entry, description)
            r = self.auth.put(u, data=i, headers={'Content-Type': 'application/xml'})
            return parseData(r.text)



    def listURL(self, value=None, entry=None, type=None, insert=None, name=None):
        """
            listURL method created api url's based on the value, entry, type.
        :param value: listID value
        :param entry: listEntry
        :param type:
        :return: API URL
        """
        a = authenticate(hostname=self.hostname, port=self.port, https=self.https)
        string = 'list'
        if value is not None:
            string = '{}/{}'.format(string, value)
        if entry is not None:
            string = '{}/entry/{}'.format(string, entry)
        if type is not None:
            string = '{}?type={}'.format(string, type)
        if name is not None:
            string = '{}&name={}'.format(string, name)
        if insert is not None:
            string = '{}/insert'.format(string)

        return a.createAppendURL(string=string)


    def listEntryDelete(self, value, position):
        """
            listEntryDelete will delete a list entry with value, description at the position:1 unless specified.
        :return: status response of the post
        """
        u = self.listURL(value=value, entry=position)
        r = self.auth.delete(u, headers={'Content-Type': 'application/xml'})
        return parseData(r.text)





    def listDelete(self, value):
        """
            listDelete will delete an entire list.
        :param value: listID value
        :return: response status.
        """
        u = self.listURL(value=value)
        r = self.auth.delete(u, headers={'Content-Type': 'application/xml'})
        return parseData(r.text)



    def listModify(self,value):
        """
            listModify will let make changes to existing list.
        :param value: listID value
        :return: response status
        """
        u = self.listURL(value=value)
        r = self.auth.put




    def listRetrive(self,value):
        """
            listRetrive will grep the existing list based on the listID
        :param value: listID value
        :return: response status
        """
        u = self.listURL(value=value)
        r = self.auth.get(u, headers={'Content-Type': 'application/xml'})
        return parseData(r.text)


    def listCreate(self, type, name):
        """
            listCreate will create a new list.
        :param type: List Type is value that defines what type of list must be created, from the documentation available
                    types are category, ip, iprange, mediatype, number, regex, string and Default is None.
        :param name: type = string, Name of new list.
        :return: response status
        """
        u = self.listURL(type=type, name=name)
        r = self.auth.post(u, headers={'Content-Type': 'application/xml'})
        return parseData(r.text)
