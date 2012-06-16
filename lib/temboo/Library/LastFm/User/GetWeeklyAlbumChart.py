
###############################################################################
#
# GetWeeklyAlbumChart
# Retrieves an album chart for a user profile, for a given date range.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWeeklyAlbumChart(Choreography):

    """
    Create a new instance of the GetWeeklyAlbumChart Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetWeeklyAlbumChart')


    def new_input_set(self):
        return GetWeeklyAlbumChartInputSet()

    def _make_result_set(self, result, path):
        return GetWeeklyAlbumChartResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeeklyAlbumChartChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWeeklyAlbumChart
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWeeklyAlbumChartInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EndTimestamp input for this choreography. ((optional, date) End timestamp at which the chart should end on, in UNIX timestamp format. This must be in the UTC time zone.)
        """
        def set_EndTimestamp(self, value):
            InputSet._set_input(self, 'EndTimestamp', value)

        """
        Set the value of the StartTimestamp input for this choreography. ((optional, date) Beginning timestamp at which the chart should start from, in UNIX timestamp format. This must be in the UTC time zone.)
        """
        def set_StartTimestamp(self, value):
            InputSet._set_input(self, 'StartTimestamp', value)

        """
        Set the value of the User input for this choreography. ((string) The last.fm username to fetch the charts of.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetWeeklyAlbumChart choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWeeklyAlbumChartResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWeeklyAlbumChartChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeeklyAlbumChartResultSet(response, path)
