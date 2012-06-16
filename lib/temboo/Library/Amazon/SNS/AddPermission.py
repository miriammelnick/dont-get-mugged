
###############################################################################
#
# AddPermission
# Creates a statement for a topic's access control policy which allows an AWS account to have access to the specified Amazon SNS actions.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddPermission(Choreography):

    """
    Create a new instance of the AddPermission Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/AddPermission')


    def new_input_set(self):
        return AddPermissionInputSet()

    def _make_result_set(self, result, path):
        return AddPermissionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddPermissionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddPermission
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddPermissionInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSAccountId input for this choreography. ((required, integer) The AWS account number of the user that will be granted access to a specified action. Enter account number omitting any dashes.)
        """
        def set_AWSAccountId(self, value):
            InputSet._set_input(self, 'AWSAccountId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the ActionName input for this choreography. ((required, string) The action you want to allow for a specified user (i.e. DeleteTopic, Publish, GetTopicAttributes, etc).)
        """
        def set_ActionName(self, value):
            InputSet._set_input(self, 'ActionName', value)

        """
        Set the value of the Label input for this choreography. ((required, string) The unique identifier for the new policy statement.)
        """
        def set_Label(self, value):
            InputSet._set_input(self, 'Label', value)

        """
        Set the value of the TopicArn input for this choreography. ((required, string) The ARN of the topic whos access control policy you want to adjust.)
        """
        def set_TopicArn(self, value):
            InputSet._set_input(self, 'TopicArn', value)


"""
A ResultSet with methods tailored to the values returned by the AddPermission choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddPermissionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddPermissionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddPermissionResultSet(response, path)
