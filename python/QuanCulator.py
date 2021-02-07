#!/usr/bin/python3
"""
QuanCulator
===========
service to enumerate quantums
-----------------------------

        _                 _
       (_)               | |
 _ __   _  __  __   ___  | |
| '__| | | \ \/ /  / _ \ | |
| |    | |  >  <  |  __/ | |
|_|    |_| /_/\_\  \___| |_|
"""
__author__    = ['Axel Ország-Krisz Dr.', 'Richárd Ádám Vécsey Dr.']
__copyright__ = "Copyright 2021, QuanCulator Project"
__credits__   = ['Axel Ország-Krisz Dr.', 'Richárd Ádám Vécsey Dr.']
__license__   = 'Copyrighted'
__version__   = '0.1'
__status__    = 'Final'



##################
# IMPORT SECTION #
##################
from bs4 import BeautifulSoup as bs
from re import findall
import requests



#############
# CONSTANTS #
#############
VALID_WEBTAG = ['http', 'https']



########
# CODE #
########
class WebObject(object):
    """
    This class holds the content of webpage
    """
    def __init__(self, link):
        """
        Initializes the WebObject
        =========================

        Parameters
        ----------
        link : str
            The URL of webpage for searching quantums.

        Attributes
        ----------
        site
        content

        Note
        ----
        It is important, that stalking innocent quantums is against the values
        of humanity and it is prohibited. Use QuanCulator if you want to handle
        these little creatures.
        """

        super(self.__class__, self).__init__()

        if link.split(':')[0] not in VALID_WEBTAG:
            raise ValueError('The format of the given link is not valid. It must be begin with http or https')

        self.__site = link
        self.__content = self.getcontent(self.__site)



    def getcontent(self, link):
        """
        Gets content from a link
        ========================

        Parameters
        ----------
        link : str
            The URL of webpage for searching quantums.

        Returns
        -------
        str
            Textual content of the URL.

        Notes
        -----
            Though the type of the return is str and it is defined as textual
            content, in fact the returned string cointains the whole content
            of the site, visible text and not directily visible elements of the
            document, like HTML tags.
        """

        raw_content = requests.get(link)
        if raw_content.status_code == 200:
            return raw_content.text
        elif raw_content.status_code == 404:
            raise RuntimeError('The given webpage is not found.')
        else:
            raise RuntimeError('Something bad happened during getting the webpage content from {}.'.format(raw_content))



    @property
    def webcontent(self):
        """
        Gets the cotent of the object
        =============================

        Returns
        -------
            Textual content of the URL.

        See also
        --------
            Notes area of getcontent() function.
        """

        return self.__content



class QuantumObject(object):
    """
    This class handles the quantums
    """
    def __init__(self, text):
        """
        Initializes the QuantumObject
        =============================

        Parameters
        ----------
        text : str
            The text content of webpage getting by WebObject

        Attributes
        ----------
        raw_text
        text_content
        low_content
        explicitquantums
        hiddenquantums
        brokenquantums
        quantumspills
        totalquantums

        Note
        ----
        It is important, that stalking innocent quantums is against the values
        of humanity and it is prohibited. Use QuanCulator if you want to handle
        these little creatures.
        """
        super(self.__class__, self).__init__()

        self.__raw_text = text
        self.__text_content = self.gettextcontent(self.__raw_text)
        self.__low_content = self.__text_content.lower()
        self.__explicitquantums = self.countofexplicitquantums()
        self.__hiddenquantums = self.countofhiddenquantums()
        self.__brokenquantums = self.countofbrokenquantums()
        self.__quantumspills = self.countofquantumspills()
        self.__totalquantums = self.(countoftotalquantums()



    def countofbrokenquantums(self):
        """
        Counts broken quantums
        ======================

        Returns
        -------
        int
            Number of broken quantums.
        """

        patterns = self.getbrokenpatterns()
        result = 0
        for pattern in patterns:
            result += len(findall(pattern, self.__low_content))
        return result



    def countofexplicitquantums(self):
        """
        Counts explicit quantums
        ========================

        Returns
        -------
        int
            Number of explicit quantums.
        """

        return self.__low_content.count('quantum')



    def countofhiddenquantums(self):
        """
        Counts hidden quantums
        ======================

        Returns
        -------
        int
            Number of hidden quantums.
        """

        return self.__raw_text.lower().count('quantum') - self.explicitquantums



    def countofquantumspills(self):
        """
        Counts quantums spills
        ======================

        Returns
        -------
        int
            Number of quantums restorable from spills.
        """

        return len(findall(self.getspillpattern(), self.__low_content))



    def countoftotalquantums(self):
        """
        Counts each kind of quantums
        ============================

        Returns
        -------
        int
            Number all quantums on a site.
        """

        return self.explicitquantums + self.hiddenquantums + self.brokenquantums + self.quantumspills



    @classmethod
    def getbrokenpatterns(cls, base='quantum'):
        """
        Gets regex patterns to find all broken quantums
        ===============================================

        Parameters
        ----------
        base : str, optional ('qunatum' if omitted)
            The word to build broken search patterns for.

        Retusns:
        --------
        list
            List of the patterns to use for regular expression rearches.

        Notes
        -----
            This method is a classmethod. Yuo can call it without instantiating
            new QuantumObject.
        """

        default_token = '[.,;:?!]? '
        result = []
        for i in range(1, len(base)):
            result.append('/' + base[:i] + default_token + base[i:] + '/')
        return result



    @classmethod
    def getspillpattern(cls, base='quantum'):
        """
        Gets a regex pattern to find spills of quantums
        ==============================================

        Parameters
        ----------
        base : str, optional ('qunatum' if omitted)
            The word to build the quantum spill search pattern for.

        Retusns:
        --------
        str
            The pattern to use for regular expression rearch.

        Notes
        -----
            This method is a classmethod. Yuo can call it without instantiating
            new QuantumObject.
        """

        len_base = len(base)
        len_base_minus_one = len_base - 1
        result = r''
        for i in range(len_base):
            result += base[i] + '[^' + base[i + 1] + ']+' if i != len_base_minus_one else base[i] + '[^' + base[0] + ']*'
        return result



    def gettextcontent(self, text):
        """
        Gets the visible text content of a HTML string
        ==============================================

        Parameters
        ----------
        text : str
            The HTML content.

        Returns
        -------
        str
            Text content.

        Notes
        -----
            This function uses BeautifulSoup. Engineers say quite often
            beautiful things used to work well. Bon appetit!
        """

        return bs(text, 'lxml').get_text()



    @property
    def brokenquantums(self):
        """
        Gets the count of broken quantums
        =================================

        Returns
        -------
        int
            The number of broken quantums.
        """

        return self.__brokenquantums



    @property
    def explicitquantums(self):
        """
        Gets the count of explicit quantums
        ===================================

        Returns
        -------
        int
            The number of explicit quantums.
        """

        return self.__explicitquantums



    @property
    def hiddenquantums(self):
        """
        Gets the count of hidden quantums
        =================================

        Returns
        -------
        int
            The number of hidden quantums.
        """

        return self.__hiddenquantums



    @property
    def quantumspills(self):
        """
        Gets the count of quantums spills
        =================================

        Returns
        -------
        int
            The number of quantum spills.
        """

        return self.__quantumspills



    @property
    def totalquantums(self):
        """
        Gets the total count of all four types of quantums
        ==================================================

        Returns
        -------
        int
            The total number of all four types of quantums.
        """

        return self.__totalquantums
