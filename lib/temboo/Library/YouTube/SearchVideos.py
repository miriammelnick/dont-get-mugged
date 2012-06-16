
###############################################################################
#
# SearchVideos
# Retrieve a list of videos matching a specified search term.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchVideos(Choreography):

    """
    Create a new instance of the SearchVideos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/YouTube/SearchVideos')


    def new_input_set(self):
        return SearchVideosInputSet()

    def _make_result_set(self, result, path):
        return SearchVideosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchVideosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchVideos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchVideosInputSet(InputSet):
        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) Specify the maximum number of results to return. The default value is 10, the maximum value is 50.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the Query input for this choreography. ((string) A search query term, including title, keyword, description, author's username, or category. Enclose in quotation marks for an for an exact match.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the StartIndex input for this choreography. ((optional, integer) Specify the first matching result to return. Uses a one-based index (the first result is 1 by default).)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)


"""
A ResultSet with methods tailored to the values returned by the SearchVideos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchVideosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The result set returned by the API call.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchVideosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchVideosResultSet(response, path)
