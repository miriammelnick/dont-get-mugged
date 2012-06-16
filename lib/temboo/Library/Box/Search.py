
###############################################################################
#
# Search
# Allows you to search items stored in your Box account.
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
        Choreography.__init__(self, temboo_session, '/Library/Box/Search')


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
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) Authorization Token retrieved by following the Oauth process described in Box.net API documentation.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the Direction input for this choreography. ((optional, string) Indicates the direction of the result sort order. Accepted values are: ASC or DESC. Defaults to "DESC".)
        """
        def set_Direction(self, value):
            InputSet._set_input(self, 'Direction', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number of the search results. Used in combination with the PerPage input for paging through many results.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) The number of results to display per page. Used in combination with the Page input for paging through many results. Defaults to 20.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)

        """
        Set the value of the Query input for this choreography. ((required, string) The text to use for the search.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Indicates how the results will be sorted. Accepted values are: relevance, name, date, or size. Defaults to "relevance".)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)


"""
A ResultSet with methods tailored to the values returned by the Search choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchResultSet(response, path)
