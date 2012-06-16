
###############################################################################
#
# IteratorHelper1
# 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class IteratorHelper1(Choreography):

    """
    Create a new instance of the IteratorHelper1 Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/Utils/IteratorHelper1')


    def new_input_set(self):
        return IteratorHelper1InputSet()

    def _make_result_set(self, result, path):
        return IteratorHelper1ResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return IteratorHelper1ChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the IteratorHelper1
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class IteratorHelper1InputSet(InputSet):
        """
        Set the value of the Count input for this choreography. ((conditional, any) )
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the XML input for this choreography. ((conditional, any) )
        """
        def set_XML(self, value):
            InputSet._set_input(self, 'XML', value)


"""
A ResultSet with methods tailored to the values returned by the IteratorHelper1 choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class IteratorHelper1ResultSet(ResultSet):
        """
        Retrieve the value for the "CurrentName" output from this choreography execution. ()
        """
        def get_CurrentName(self):
            return self._output.get('CurrentName', None)
        """
        Retrieve the value for the "CurrentValue" output from this choreography execution. ()
        """
        def get_CurrentValue(self):
            return self._output.get('CurrentValue', None)

class IteratorHelper1ChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return IteratorHelper1ResultSet(response, path)
