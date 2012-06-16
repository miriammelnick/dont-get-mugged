
###############################################################################
#
# GetTrendingVideos
# Retrieves Movies and Trailers videos that have had the greatest increases in popularity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTrendingVideos(Choreography):

    """
    Create a new instance of the GetTrendingVideos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/YouTube/GetTrendingVideos')


    def new_input_set(self):
        return GetTrendingVideosInputSet()

    def _make_result_set(self, result, path):
        return GetTrendingVideosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTrendingVideosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTrendingVideos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTrendingVideosInputSet(InputSet):
        """
        Set the value of the PaidContent input for this choreography. ((optional, boolean) Restrict the search to only include paid content ("true") or to include both paid and free content ("false", the default).)
        """
        def set_PaidContent(self, value):
            InputSet._set_input(self, 'PaidContent', value)

        """
        Set the value of the Region input for this choreography. ((optional, string) Restrict search to movies viewable in a specific region (defaults to "US"). Required for paid-content-only searches.)
        """
        def set_Region(self, value):
            InputSet._set_input(self, 'Region', value)


"""
A ResultSet with methods tailored to the values returned by the GetTrendingVideos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTrendingVideosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The result set returned by the API call.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTrendingVideosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTrendingVideosResultSet(response, path)
