
###############################################################################
#
# PhotoDetails
# Retrieves details of a photo. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PhotoDetails(Choreography):

    """
    Create a new instance of the PhotoDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Photos/PhotoDetails')


    def new_input_set(self):
        return PhotoDetailsInputSet()

    def _make_result_set(self, result, path):
        return PhotoDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PhotoDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PhotoDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PhotoDetailsInputSet(InputSet):
        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the PhotoID input for this choreography. ((required, string) The ID of the photo to get details for.)
        """
        def set_PhotoID(self, value):
            InputSet._set_input(self, 'PhotoID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the PhotoDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PhotoDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PhotoDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PhotoDetailsResultSet(response, path)
