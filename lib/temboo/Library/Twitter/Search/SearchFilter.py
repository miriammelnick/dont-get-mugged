
###############################################################################
#
# SearchFilter
# Allows you to search Twitter for a keyword and filter out unwanted Tweets from search results.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchFilter(Choreography):

    """
    Create a new instance of the SearchFilter Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Search/SearchFilter')


    def new_input_set(self):
        return SearchFilterInputSet()

    def _make_result_set(self, result, path):
        return SearchFilterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchFilterChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchFilter
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchFilterInputSet(InputSet):
        """
        Set the value of the Filter input for this choreography. ((string) A search string to use to filter out unwanted Tweets.)
        """
        def set_Filter(self, value):
            InputSet._set_input(self, 'Filter', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to return. Can be used to page through many results. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ResultsPerPage input for this choreography. ((integer) The number of results to return. Defaults to 20.)
        """
        def set_ResultsPerPage(self, value):
            InputSet._set_input(self, 'ResultsPerPage', value)

        """
        Set the value of the SearchString input for this choreography. ((string) A string to use as the search query)
        """
        def set_SearchString(self, value):
            InputSet._set_input(self, 'SearchString', value)


"""
A ResultSet with methods tailored to the values returned by the SearchFilter choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchFilterResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Twitter)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchFilterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchFilterResultSet(response, path)
