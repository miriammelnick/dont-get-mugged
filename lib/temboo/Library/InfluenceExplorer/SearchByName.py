
###############################################################################
#
# SearchByName
# Searches for politicians, individuals, or organizations with the given name. Returns basic information about the the contributions to and from the entity that is specified.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByName(Choreography):

    """
    Create a new instance of the SearchByName Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/SearchByName')


    def new_input_set(self):
        return SearchByNameInputSet()

    def _make_result_set(self, result, path):
        return SearchByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByName
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByNameInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Sunlight Data Services.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Search input for this choreography. ((required, string) The query string.)
        """
        def set_Search(self, value):
            InputSet._set_input(self, 'Search', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByName choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByNameResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Influence Explorer.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByNameResultSet(response, path)
