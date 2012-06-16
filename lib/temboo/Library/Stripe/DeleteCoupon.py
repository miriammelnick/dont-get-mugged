
###############################################################################
#
# DeleteCoupon
# Deletes a specified coupon.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteCoupon(Choreography):

    """
    Create a new instance of the DeleteCoupon Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/DeleteCoupon')


    def new_input_set(self):
        return DeleteCouponInputSet()

    def _make_result_set(self, result, path):
        return DeleteCouponResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCouponChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteCoupon
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteCouponInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the CouponId input for this choreography. ((optional, string) The unique identifier of the coupon you wish to delete)
        """
        def set_CouponId(self, value):
            InputSet._set_input(self, 'CouponId', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteCoupon choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteCouponResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteCouponChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteCouponResultSet(response, path)
