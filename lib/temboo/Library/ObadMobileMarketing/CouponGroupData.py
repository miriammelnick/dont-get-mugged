
###############################################################################
#
# CouponGroupData
# Allows you to add or remove a coupon from a coupon group.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CouponGroupData(Choreography):

    """
    Create a new instance of the CouponGroupData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/CouponGroupData')


    def new_input_set(self):
        return CouponGroupDataInputSet()

    def _make_result_set(self, result, path):
        return CouponGroupDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CouponGroupDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CouponGroupData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CouponGroupDataInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ClientID input for this choreography. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the CouponGroupID input for this choreography. ((integer) The ID of the coupongroup you need to update)
        """
        def set_CouponGroupID(self, value):
            InputSet._set_input(self, 'CouponGroupID', value)

        """
        Set the value of the CouponID input for this choreography. ((integer) The ID of the coupon you need to update)
        """
        def set_CouponID(self, value):
            InputSet._set_input(self, 'CouponID', value)

        """
        Set the value of the Endpoint input for this choreography. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Mode input for this choreography. ((optional, boolean) Specify 0 for removing or 1 for adding. Defaults to 1.)
        """
        def set_Mode(self, value):
            InputSet._set_input(self, 'Mode', value)

        """
        Set the value of the CSVData input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the CouponGroupData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CouponGroupDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Obad)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CouponGroupDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CouponGroupDataResultSet(response, path)
