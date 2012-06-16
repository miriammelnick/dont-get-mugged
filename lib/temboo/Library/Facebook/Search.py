
###############################################################################
#
# Search
# Search public objects across the social graph.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Search(Choreography):

    """
    Create a new instance of the Search Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Search')


    def new_input_set(self):
        return SearchInputSet()

    def _make_result_set(self, result, path):
        return SearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Search
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The access token retrieved from the final step of the OAuth process. This is required for certain object types such as "user".)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Center input for this choreography. ((optional, string) The coordinates for a place (such as 37.76,122.427). Used only when specifying an object ype of "place".)
        """
        def set_Center(self, value):
            InputSet._set_input(self, 'Center', value)

        """
        Set the value of the Distance input for this choreography. ((optional, integer) The distance search parameter used only when specifying an object type of "place". Defaults to 1000.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the ObjectType input for this choreography. ((required, string) The type of object to search for. Accepted values are: post, user, page, event, group, place, or checkin.)
        """
        def set_ObjectType(self, value):
            InputSet._set_input(self, 'ObjectType', value)

        """
        Set the value of the Query input for this choreography. ((required, string) The Facebook query term to send in the request.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Search choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchResultSet(response, path)
