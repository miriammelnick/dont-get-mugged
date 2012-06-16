
###############################################################################
#
# IteratorHelper2
# 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class IteratorHelper2(Choreography):

    """
    Create a new instance of the IteratorHelper2 Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/Utils/IteratorHelper2')


    def new_input_set(self):
        return IteratorHelper2InputSet()

    def _make_result_set(self, result, path):
        return IteratorHelper2ResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return IteratorHelper2ChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the IteratorHelper2
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class IteratorHelper2InputSet(InputSet):
        """
        Set the value of the XML input for this choreography. ((conditional, any) )
        """
        def set_XML(self, value):
            InputSet._set_input(self, 'XML', value)

        """
        Set the value of the CurrentName input for this choreography. ((conditional, any) )
        """
        def set_CurrentName(self, value):
            InputSet._set_input(self, 'CurrentName', value)

        """
        Set the value of the RowCount input for this choreography. ((conditional, any) )
        """
        def set_RowCount(self, value):
            InputSet._set_input(self, 'RowCount', value)


"""
A ResultSet with methods tailored to the values returned by the IteratorHelper2 choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class IteratorHelper2ResultSet(ResultSet):
        """
        Retrieve the value for the "Key" output from this choreography execution. ()
        """
        def get_Key(self):
            return self._output.get('Key', None)
        """
        Retrieve the value for the "Value" output from this choreography execution. ()
        """
        def get_Value(self):
            return self._output.get('Value', None)

class IteratorHelper2ChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return IteratorHelper2ResultSet(response, path)
