
###############################################################################
#
# MonitorInstances
# Enable monitoring for a specified instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MonitorInstances(Choreography):

    """
    Create a new instance of the MonitorInstances Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/MonitorInstances')


    def new_input_set(self):
        return MonitorInstancesInputSet()

    def _make_result_set(self, result, path):
        return MonitorInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MonitorInstancesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MonitorInstances
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MonitorInstancesInputSet(InputSet):
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
        Set the value of the InstanceId input for this choreography. ((required, string) The id for the instance you want to monitor.)
        """
        def set_InstanceId(self, value):
            InputSet._set_input(self, 'InstanceId', value)


"""
A ResultSet with methods tailored to the values returned by the MonitorInstances choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MonitorInstancesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MonitorInstancesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MonitorInstancesResultSet(response, path)
