
###############################################################################
#
# GetRecommendedEvents
# Retrieves a paginated list of all events recommended to a user by Last.fm, based on their listening profile. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecommendedEvents(Choreography):

    """
    Create a new instance of the GetRecommendedEvents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetRecommendedEvents')


    def new_input_set(self):
        return GetRecommendedEventsInputSet()

    def _make_result_set(self, result, path):
        return GetRecommendedEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecommendedEventsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecommendedEvents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecommendedEventsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((string) Your Last.fm API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to fetch. Defaults to first page.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the SessionKey input for this choreography. ((string) The session key retrieved in the last step of the authorization process.)
        """
        def set_SessionKey(self, value):
            InputSet._set_input(self, 'SessionKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecommendedEvents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecommendedEventsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecommendedEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecommendedEventsResultSet(response, path)
