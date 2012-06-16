
###############################################################################
#
# EditCoupon
# Allows you to create a new coupon or update an existing one.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EditCoupon(Choreography):

    """
    Create a new instance of the EditCoupon Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/EditCoupon')


    def new_input_set(self):
        return EditCouponInputSet()

    def _make_result_set(self, result, path):
        return EditCouponResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditCouponChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EditCoupon
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EditCouponInputSet(InputSet):
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
        Set the value of the CouponId input for this choreography. ((integer) The ID of the coupon you need to update.  In creation mode, leave this blank, and the ID will be returned in the response.)
        """
        def set_CouponId(self, value):
            InputSet._set_input(self, 'CouponId', value)

        """
        Set the value of the Desc1 input for this choreography. ((string) Description at the TOP of the coupon)
        """
        def set_Desc1(self, value):
            InputSet._set_input(self, 'Desc1', value)

        """
        Set the value of the Desc2 input for this choreography. ((string) Description at the BOTTOM line 1 of the coupon)
        """
        def set_Desc2(self, value):
            InputSet._set_input(self, 'Desc2', value)

        """
        Set the value of the Desc3 input for this choreography. ((string) Description of the BOTTOM line 2 of the coupon)
        """
        def set_Desc3(self, value):
            InputSet._set_input(self, 'Desc3', value)

        """
        Set the value of the Endpoint input for this choreography. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the From input for this choreography. ((date) The first date that the coupon is available (formatted like YYYY/MM/DD))
        """
        def set_From(self, value):
            InputSet._set_input(self, 'From', value)

        """
        Set the value of the Mode input for this choreography. ((optional, boolean) Specify the writing mode. Use '0' for creating or '1'  for updating. Defaults to 0.)
        """
        def set_Mode(self, value):
            InputSet._set_input(self, 'Mode', value)

        """
        Set the value of the Title input for this choreography. ((string) The title of the coupon that will be only used for the console)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the To input for this choreography. ((date) The final date that the coupon is available (formatted like YYYY/MM/DD))
        """
        def set_To(self, value):
            InputSet._set_input(self, 'To', value)

        """
        Set the value of the UseOnce input for this choreography. ((optional, boolean) Use '1' for use and burn coupon one time only and '0' for unlimited use and burn. Defaults to 0.)
        """
        def set_UseOnce(self, value):
            InputSet._set_input(self, 'UseOnce', value)


"""
A ResultSet with methods tailored to the values returned by the EditCoupon choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EditCouponResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Obad)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EditCouponChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditCouponResultSet(response, path)
