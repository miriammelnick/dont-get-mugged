
###############################################################################
#
# SearchProjectsByKeyword
# Allows you to projects subjects by keyword.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchProjectsByKeyword(Choreography):

    """
    Create a new instance of the SearchProjectsByKeyword Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DonorsChoose/SearchProjectsByKeyword')


    def new_input_set(self):
        return SearchProjectsByKeywordInputSet()

    def _make_result_set(self, result, path):
        return SearchProjectsByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchProjectsByKeywordChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchProjectsByKeyword
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchProjectsByKeywordInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((optional, string) The APIKey provided by Donor's Choose. Defaults to the test  APIKey 'DONORSCHOOSE'.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Keyword input for this choreography. ((required, string) Allows you to search for subjects using keyword search)
        """
        def set_Keyword(self, value):
            InputSet._set_input(self, 'Keyword', value)

        """
        Set the value of the Max input for this choreography. ((optional, integer) The max number of projects to return. Can return up to 50 rows at a time. Defaults to 10 when left empty.)
        """
        def set_Max(self, value):
            InputSet._set_input(self, 'Max', value)


"""
A ResultSet with methods tailored to the values returned by the SearchProjectsByKeyword choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchProjectsByKeywordResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Donor's Choose)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchProjectsByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchProjectsByKeywordResultSet(response, path)
