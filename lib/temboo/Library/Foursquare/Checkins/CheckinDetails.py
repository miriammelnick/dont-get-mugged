
###############################################################################
#
# CheckinDetails
# Returns details of a checkin.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CheckinDetails(Choreography):

    """
    Create a new instance of the CheckinDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/CheckinDetails')


    def new_input_set(self):
        return CheckinDetailsInputSet()

    def _make_result_set(self, result, path):
        return CheckinDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CheckinDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CheckinDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CheckinDetailsInputSet(InputSet):
        """
        Set the value of the CheckinID input for this choreography. ((required, string) The ID of the checkin to retrieve additional information for.)
        """
        def set_CheckinID(self, value):
            InputSet._set_input(self, 'CheckinID', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Signature input for this choreography. ((optional, string) When checkins are sent to public feeds such as Twitter, foursquare appends a signature to them (s=XXXXXX). The same value can be used here.)
        """
        def set_Signature(self, value):
            InputSet._set_input(self, 'Signature', value)


"""
A ResultSet with methods tailored to the values returned by the CheckinDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CheckinDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CheckinDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CheckinDetailsResultSet(response, path)
