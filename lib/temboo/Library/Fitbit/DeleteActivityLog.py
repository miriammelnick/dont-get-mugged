
###############################################################################
#
# DeleteActivityLog
# Deletes a specified activity log entry.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteActivityLog(Choreography):

    """
    Create a new instance of the DeleteActivityLog Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/DeleteActivityLog')


    def new_input_set(self):
        return DeleteActivityLogInputSet()

    def _make_result_set(self, result, path):
        return DeleteActivityLogResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteActivityLogChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteActivityLog
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteActivityLogInputSet(InputSet):
        """
        Set the value of the ActivityLogId input for this choreography. ((integer) The id of the activity log you want to delete. The Id is returned in the LogActivity response.)
        """
        def set_ActivityLogId(self, value):
            InputSet._set_input(self, 'ActivityLogId', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) The format that you want the response to be in: xml or json. Defaults to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((string) The Oauth Consumer Key provided by Fitbit after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((string) The Oauth Consumer Secret provided by Fitbit after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided. )
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteActivityLog choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteActivityLogResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Fitbit in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteActivityLogChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteActivityLogResultSet(response, path)
