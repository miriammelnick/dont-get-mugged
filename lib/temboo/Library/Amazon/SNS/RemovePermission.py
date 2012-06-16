
###############################################################################
#
# RemovePermission
# Removes the statement from a topic's access control policy that was created with the AddPermission action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RemovePermission(Choreography):

    """
    Create a new instance of the RemovePermission Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/RemovePermission')


    def new_input_set(self):
        return RemovePermissionInputSet()

    def _make_result_set(self, result, path):
        return RemovePermissionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemovePermissionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RemovePermission
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RemovePermissionInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the Label input for this choreography. ((required, string) The unique identifier for the policy statement that you want to delete.)
        """
        def set_Label(self, value):
            InputSet._set_input(self, 'Label', value)

        """
        Set the value of the TopicArn input for this choreography. ((required, string) The ARN of the topic that has an access control policy you want to adjust.)
        """
        def set_TopicArn(self, value):
            InputSet._set_input(self, 'TopicArn', value)


"""
A ResultSet with methods tailored to the values returned by the RemovePermission choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RemovePermissionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RemovePermissionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RemovePermissionResultSet(response, path)
