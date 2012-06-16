
###############################################################################
#
# Done
# Returns an array of users have done this tip.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Done(Choreography):

    """
    Create a new instance of the Done Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Tips/Done')


    def new_input_set(self):
        return DoneInputSet()

    def _make_result_set(self, result, path):
        return DoneResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DoneChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Done
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DoneInputSet(InputSet):
        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to return, up to 200.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) Your Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Used to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TipID input for this choreography. ((required, string) The id of a tip to get users who have marked the tip as done.)
        """
        def set_TipID(self, value):
            InputSet._set_input(self, 'TipID', value)


"""
A ResultSet with methods tailored to the values returned by the Done choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DoneResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DoneChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DoneResultSet(response, path)
