
###############################################################################
#
# CampaignSearch
# Search for ad campaigns using IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CampaignSearch(Choreography):

    """
    Create a new instance of the CampaignSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AdMob/CampaignSearch')


    def new_input_set(self):
        return CampaignSearchInputSet()

    def _make_result_set(self, result, path):
        return CampaignSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CampaignSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CampaignSearchInputSet(InputSet):
        """
        Set the value of the CampaignID input for this choreography. ((required, string) Search for ad campaigns using this ID.)
        """
        def set_CampaignID(self, value):
            InputSet._set_input(self, 'CampaignID', value)

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
        Set the value of the Token input for this choreography. ((required, string) Enter user token.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the CampaignSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CampaignSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from AdMob in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CampaignSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CampaignSearchResultSet(response, path)
