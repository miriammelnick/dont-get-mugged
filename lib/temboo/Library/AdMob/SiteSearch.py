
###############################################################################
#
# SiteSearch
# Search for sites by specifying their ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SiteSearch(Choreography):

    """
    Create a new instance of the SiteSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AdMob/SiteSearch')


    def new_input_set(self):
        return SiteSearchInputSet()

    def _make_result_set(self, result, path):
        return SiteSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SiteSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SiteSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SiteSearchInputSet(InputSet):
        """
        Set the value of the ClientKey input for this choreography. ((required, string) Enter user client key.)
        """
        def set_ClientKey(self, value):
            InputSet._set_input(self, 'ClientKey', value)

        """
        Set the value of the IncludeDeleted input for this choreography. ((optional, boolean) If set to 1, ad groups that have been deleted will be included in the search result.)
        """
        def set_IncludeDeleted(self, value):
            InputSet._set_input(self, 'IncludeDeleted', value)

        """
        Set the value of the SiteID input for this choreography. ((optional, string) Search for a site matching this ID.)
        """
        def set_SiteID(self, value):
            InputSet._set_input(self, 'SiteID', value)

        """
        Set the value of the Token input for this choreography. ((required, string) Enter user token.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the SiteSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SiteSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from AdMob in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SiteSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SiteSearchResultSet(response, path)
