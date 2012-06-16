
###############################################################################
#
# Delta
# Allows you keep up with changes to files and folders in a user's Dropbox.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Delta(Choreography):

    """
    Create a new instance of the Delta Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/Delta')


    def new_input_set(self):
        return DeltaInputSet()

    def _make_result_set(self, result, path):
        return DeltaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeltaChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Delta
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeltaInputSet(InputSet):
        """
        Set the value of the Cursor input for this choreography. ((optional, string) A string that is used to keep track of your current state. On the next call pass in this value to return delta entries that have been recorded since the cursor was returned.)
        """
        def set_Cursor(self, value):
            InputSet._set_input(self, 'Cursor', value)

        """
        Set the value of the Locale input for this choreography. ((optional, string) The metadata returned will have its size field translated based on the given locale.)
        """
        def set_Locale(self, value):
            InputSet._set_input(self, 'Locale', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The OAuth Consumer Key provided by Dropbox after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Drop Box after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The OAuth Token Secret retrieved during the OAuth process.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The OAuth Token retrieved during the OAuth process.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Delta choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeltaResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeltaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeltaResultSet(response, path)
