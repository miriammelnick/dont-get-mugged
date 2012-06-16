
###############################################################################
#
# DescribeInstances
# Returns information on EC2 instances associated with your AWS account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DescribeInstances(Choreography):

    """
    Create a new instance of the DescribeInstances Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeInstances')


    def new_input_set(self):
        return DescribeInstancesInputSet()

    def _make_result_set(self, result, path):
        return DescribeInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeInstancesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DescribeInstances
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DescribeInstancesInputSet(InputSet):
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
        Set the value of the InstanceId input for this choreography. ((optional, string) The ID of the instance you want to return. Returns all instances if this parameter is not specified.)
        """
        def set_InstanceId(self, value):
            InputSet._set_input(self, 'InstanceId', value)


"""
A ResultSet with methods tailored to the values returned by the DescribeInstances choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DescribeInstancesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DescribeInstancesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeInstancesResultSet(response, path)
